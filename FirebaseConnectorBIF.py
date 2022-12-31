# FirebaseConnectorBIF.py will be used to connect systemd like Hubspot, Google Analytics, and Comm100 to Firebase
# Update Friday 10-14: removed firebaseConfig parameters from file, they are now called from .env

import pyrebase
import pandas as pd
from datetime import date  # Return to this later, for dates/times -> https://dateutil.readthedocs.io/en/stable/
from dotenv import load_dotenv
load_dotenv()
import os
""" 
csv was NOT installed w/pip3 because the module is already in PyCharm
import csv
"""

# Set up Firebase
firebaseConfig = {       # These are Bryan's Firebase credentials
    "apiKey": os.environ.get("apiKey2"),
    "authDomain": os.environ.get("authDomain2"),
    "projectId": os.environ.get("projectId2"),
    "storageBucket": os.environ.get("storageBucket2"),
    "messagingSenderId": os.environ.get("messagingSenderId2"),
    "appId": os.environ.get("appId2"),
    "databaseURL": os.environ.get("databaseURL2")
}

firebase = pyrebase.initialize_app(firebaseConfig)  # create a firebase app using credentials above
db = firebase.database()  # get the instance of realtime database using url  "databaseURL" above

# Create a JSON UserObject that will be used to interact with Firebase
# Assign types and temporary data to variables used by the UserObject below
# BIFQ: do I need this step, or to assign temporary data??
# BIFQ: or can I just put type assignments into the UserObject below, and new variables would be defined implicitly?
VarUniqueID: int = 99
VarFirst: str = "FirstTemp"
VarMid: str = "MidTemp"
VarLast: str = "LastTemp"
VarFatherName: str = "FatherNameTemp"
VarPhoneNumber: str = "PhoneNumberTemp"
VarAge: int = 9999
print("-------------")

# Initialize the JSON UserObject with the temporary variables
UserObject = {
    "UniqueID": int(VarUniqueID),
    "FullName": {
        "FirstName": VarFirst,
        "MidName": VarMid,
        "lastName": VarLast
    },
    "FatherName": VarFatherName,
    "PhoneNumber": VarPhoneNumber,
    "Age": VarAge
}

# User Interface: Allow User to choose an operation (reading or writing to Firebase)
WelcomeString ="""
Welcome to the Test Database
Enter 1 to add a record(s) using a .csv file
Enter 2 to add a record manually
Enter 3 to retrieve a record
Enter 4 to end the program
"""
print(WelcomeString)
UserChoice = input()

# MAIN LOOP: Based on UserChoice, execute respective operations

# BRANCH 1: ENTER RECORD(S) USING .CSV
if int(UserChoice) == 1:
    print("You've selected 'Enter 1 to add a record(s) using a .csv file'")
    print("Please enter your file name, including the suffix .csv")
    # using file: FirebaseTestData.csv
    VarFileName = input()

    # Create DataFrame for the .csv test data
    df_fromCSV = pd.read_csv(VarFileName, engine='python')
    # this was a hardcoded example instead of using "VarFileName" -> df_fromCSV = pd.read_csv("FirebaseTestData.csv", engine='python')
    # Return to this later, a method for reading a dictionary of csv column headings -> df_DictionaryLabels = pd.read_csv("DictionaryLabels.csv", engine='python')
    print("This is the DataFrame imported from the CSV file -->  ")
    print(df_fromCSV)

    # Create JSON objects from each CSV record and write each object to Firebase
    for loop2 in range(
            len(df_fromCSV)):  # for reference: df_temp loops columns, df_temp.index loops rows, no () or [] needed here

        # Assign temporary variables to fill the UserObject that will be sent to Firebase
        print(df_fromCSV.at[loop2, "UniqueID"])
        VarUniqueID = int(df_fromCSV.at[loop2, "UniqueID"])       # UniqueID is the .csv column header
        print('VarUniqueID = ', VarUniqueID)
        VarFirst = df_fromCSV.at[loop2, "First"]              # First is the .csv column header
        print('VarFirst = ', VarFirst)
        VarMid = df_fromCSV.at[loop2, "Mid"]                  # Mid is the .csv column header
        print('VarMid = ', VarMid)
        VarLast = df_fromCSV.at[loop2, "Last"]                # Last is the .csv column header
        print('VarLast = ', VarLast)
        VarFatherName = df_fromCSV.at[loop2, "FatherName"]    # FatherName is the .csv column header
        print('VarFatherName = ', VarFatherName)
        VarPhoneNumber = df_fromCSV.at[loop2, "PhoneNumber"]  # PhoneNumber is the .csv column header
        print('VarPhoneNumber = ', VarPhoneNumber)
        VarAge = int(df_fromCSV.at[loop2, "Age"]    )              # Age is the .csv column header
        print('VarAge = ', VarAge)
        print("-------------")

        # Fill the UserObject with rgw loop variables
        UserObject = {
            "UniqueID": VarUniqueID,
            "FullName": {
                "Mid": VarMid,
                "First": VarFirst,
                "last": VarLast
            },
            "FatherName": VarFatherName,
            "PhoneNumber": str(VarPhoneNumber),
            "Age": int(VarAge)
        }
        print(loop2, "This is the User Object -->  ")
        print(UserObject)
        print("-------------")

        # Push the UserObject up to Firebase
        VarFirebaseKey = "bkey" + str(loop2)
        db.push(
            UserObject)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well
        db.child(VarFirebaseKey).set(
            UserObject)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key

    print("All finished. The program will now end")
    quit()

# BRANCH 2: ENTER RECORD MANUALLY
elif int(UserChoice) == 2:
    print("You've selected 'Enter 2 to add a record manually'")

    print("Please enter a UniqueID for the record")
    VarUniqueID = input()
    print("You entered", VarUniqueID)

    print("Please enter 3 values: First Name, Middle Name, and Last Name (separate with spaces, not commas")
    VarFirst, VarMid, VarLast = input().split()
    print("You entered First Name: ", VarFirst)
    print("You entered Middle Name: ", VarMid)
    print("You entered Last Name: ", VarLast)

    print("Please enter Father's name")
    VarFatherName = input()
    print("You entered", VarFatherName)

    print("Please enter phone number in format xxx-yyy-zzzz")
    VarPhoneNumber = input()
    print("You entered", VarPhoneNumber)

    print("Please enter the person's age")
    VarAge = input()
    print("You entered", VarAge)

    # Fill the UserObject with the manually entered loop variables
    UserObject = {
        "UniqueID": VarUniqueID,
        "FullName": {
            "Mid": VarMid,
            "First": VarFirst,
            "last": VarLast
        },
        "FatherName": VarFatherName,
        "PhoneNumber": str(VarPhoneNumber),
        "Age": int(VarAge)
    }
    print("This is the manual User Object -->  ")
    print(UserObject)
    print("-------------")

    # Push the UserObject up to Firebase
    VarFirebaseKey = "bkey" + str(VarUniqueID)
    db.push(
        UserObject)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well
    db.child(VarFirebaseKey).set(
        UserObject)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key

    print("All finished. The program will now end")
    quit()

# BRANCH 3: RETRIEVE A RECORD
elif int(UserChoice) == 3:
    print("You've selected 'Enter 3 to retrieve a record'")

    string = """
    To retrieve a record, enter the number of the field type for your search:
    Enter 1 to search by UniqueID
    (NOTE: the following choices are not operational yet - only search by unique ID)
    (NOTE: Suggested unique ID's for testing: -NDYUCz5R3FPs-hswt-G , bkey555)
    Enter 2 to search by First Name
    Enter 3 to search by Middle Name
    Enter 4 to search by Last Name
    Enter 5 to search by Phone Number
    Enter 6 to search by Age
    Enter 7 to end the program
    """
    print(string)
    SearchChoice = input()
    print("You entered search field ", SearchChoice)

    # SUB-BRANCHES FOR "RETRIEVE A RECORD"
    if int(SearchChoice) == 1:
        print("Please enter the UniqueID")
        VarSearchUniqueID = input()
        myObj = db.child(VarSearchUniqueID).get()
        print(myObj.val())
        print('_______________')

        for loop3 in myObj.each():
            print(loop3.key(),loop3.val())  # from documentation: Morty, {name": "Mortimer 'Morty' Smith"}
            # print(loop3.val())

            """
            BIFQ: 
            REFERENCE DOCS: https://github.com/thisbejim/Pyrebase 
            
            How do I query using a field value (ie, LastName ? )
            How does myObj (on line 201) know what fields it is retrieving in the JSON object, so that I can query by field?
            
            What does .child method do? 
            
            
            
            """
    else:
        print("temp - ignore this")

    print("All finished. The program will now end")
    quit()

# BRANCH 4: EXIT FROM PROGRAM
else:  # Don't need this --> int(UserChoice) == 4
    print("You've selected 'Enter 4 to end the program'")
    quit()

