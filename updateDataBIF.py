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

data = {"Mid": "Robert", "age": "98"}  # new object for the unique key we used in createData.py file
db.child("BryanKeyTest3").update(data)  # grab object using "mykey" and then update its data with new object

db.child("myKey4").child("name").set("field update")  # we can also set value for a field inside object using set
# function, if key not found in our case "name" then set function create one

data = {"name": "Ahsan", "age": "22"}  # new object for the unique key we used in createData.py file
db.child("myKey3").update(data)  # grab object using "mykey" and then update its data with new object

