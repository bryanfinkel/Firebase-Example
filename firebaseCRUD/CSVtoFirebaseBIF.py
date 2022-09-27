# BIF: Modification Record

import pyrebase

""" 
csv was NOT installed w/pip3 because the module is already in PyCharm

import csv
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import os

# BIF Debugging, look into this for dates/times -> https://dateutil.readthedocs.io/en/stable/
"""
from datetime import date
import pandas as pd

firebaseConfig = {
    # This is Bryan's Firebase config data

    "apiKey": "AIzaSyCJns_OH8FlIA8g7MlGxJhOqf---q2bzgc",
    "authDomain": "test0922-52866.firebaseapp.com",
    "projectId": "test0922-52866",
    "storageBucket": "test0922-52866.appspot.com",
    "messagingSenderId": "28451809789",
    "appId": "1:28451809789:web:26ed0b26687d0576abd194",
    "databaseURL": "https://test0922-52866-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)  # create a firebase app
db = firebase.database()  # get the instance of realtime database using url above
# BIF: Q Does this create a new database every time? How do we create a database one time, and then use the same database
#   in the future instead of creating a new datbase every time?

# BIF new code below ------------------------
today = date.today()
# Following date and time variables received errors, need to fix this later
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
print(today)

# STEP 1: Create DataFrame for the .csv test data
df_fromCSV = pd.read_csv("FirebaseTestData.csv", engine='python')
# df_DictionaryLabels = pd.read_csv("DictionaryLabels.csv", engine='python') - Come back to this later
print(df_fromCSV)
# print(df_DictionaryLabels)
print("###")

# STEP 2: Create JSON objects and write each one to Firebase

for loop2 in range(
                len(df_fromCSV)):  # df_temp loops columns, df_temp.index loops rows, no () or [] needed here

    # Assign temporary variables to fill the UserObject that will be sent to Firebase
    VarUniqueID = df_fromCSV.at[loop2, "UniqueID"]
    print('VarUniqueID = ', VarUniqueID)
    VarMid = df_fromCSV.at[loop2, "Mid"]
    print('VarMid = ',VarMid)
    Varfirst = df_fromCSV.at[loop2, "first"]
    print('Varfirst = ',Varfirst)
    VarLast = df_fromCSV.at[loop2, "Last"]
    print('VarLast = ',VarLast)
    VarfatherName = df_fromCSV.at[loop2, "fatherName"]
    print('VarfatherName = ',VarfatherName)
    VarPhoneNumber = df_fromCSV.at[loop2, "PhoneNumber"]
    print('VarPhoneNumber = ',VarPhoneNumber)
    VarAge = df_fromCSV.at[loop2, "Age"]
    print('VarAge = ',VarAge)
    print("-------------")

    # Fill the UserObject with the temporary variables
    UserObject = {
        "UniqueID": int(VarUniqueID),
        "fullName": {
            "Mid": VarMid,
            "first": Varfirst,
            "last": VarLast
        },
        "fatherName": VarfatherName,
        "PhoneNumber": str(VarPhoneNumber),
        "Age": int(VarAge)
    }
    print(UserObject)
    print("-------------")

    # Push the UserObject up to Firebase
    VarFirebaseKey = "akey"+str(loop2)
    db.push(UserObject)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well
    db.child(VarFirebaseKey).set(UserObject)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key

""" 
OLD SCRAPS BELOW ARE FOR REFERENCE, IGNORE THIS FOR NOW
data = {"name": "jerry"}  # create a simple object to store
db.push(data)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well

data = {"name": "John"}  # another simple object to store but this time with our own key
db.child("myKey").set(data)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key

# BIF: create an object, then read data into the object from command line, then push the object to firebase:
# BIF: STEP 1: Create the object
UserObject = {
    "UniqueID": 999,
    "fullName": {
        "Mid": "Mark",
        "first": "Fred",
        "last": "Jones"
    },
    "fatherName": "Jones",
    "PhoneNumber":"914-933-7525",
    "Age":25
}
# BIF: STEP 2: Test the modification of the object using command line inputs

# BIF: Print the initial object, then input a change
print('initial object is', UserObject)

print("to change the object, please input a Mid name")
Mid_input = input()
print('your change is ',Mid_input)

# BIF: use the input data to change the object, and print out the updated object
UserObject['fullName']['Mid'] = Mid_input
print('after new imput, the object is', UserObject)

# BIF: Now push entire object to Firebase

db.push(UserObject)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well
db.child("BryanKeyTest3").set(UserObject)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key

# BIF: read data from .CSV, then push the data in JSON format to firebase:
"""