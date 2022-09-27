
"""
THIS FILE IS BASED ON A TUTORIAL
# https://www.geeksforgeeks.org/select-rows-columns-by-name-or-index-in-pandas-dataframe-using-loc-iloc/
OTHER SIMILAR TUTORIALS ON INDEXING DATAFRAMES:
https://pythonexamples.org/pandas-dataframe-access-a-single-value/
https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
https://www.learnbyexample.org/python-nested-dictionary/
https://www.dataquest.io/blog/tutorial-indexing-dataframes-in-pandas/
"""

# import pandas
import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
			('Saumya', 32, 'Delhi', 25000),
			('Aaditya', 25, 'Mumbai', 40000),
			('Saumya', 32, 'Delhi', 35000),
			('Saumya', 32, 'Delhi', 30000),
			('Saumya', 32, 'Mumbai', 20000),
			('Aaditya', 40, 'Dehradun', 24000),
			('Seema', 32, 'Delhi', 70000)
			]

# Create a DataFrame object from list
df = pd.DataFrame(employees,
				columns =['Name', 'Age',
						'City', 'Salary'])
# Show the dataframe
df
# BIF WHERE did that dataframe get shown without using a print statement ???

print('--------')
print(df)

# Using the operator []
# to select a column
result = df["City"]

# Show the dataframe
result
print('--------')
print(result)

# Using the operator [] to
# select multiple columns
result = df[["Age", "Salary","Name", "Name"]]

# Show the dataframe
result
print('--------')
print(result)

# Select Rows by Name in Pandas DataFrame using loc

# Create a DataFrame object from list
df = pd.DataFrame(employees,
				columns =['Name', 'Age',
				'City', 'Salary'])

# Set 'Name' column as index
# on a Dataframe
df.set_index("Name", inplace = True)

# Using the operator .loc[]
# to select single row
result = df.loc["Stuti"]

# Show the dataframe
result

print('-------- Stuti ')
print(result)
print(result[0])

