# BIF: Modification Record

import pyrebase

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
