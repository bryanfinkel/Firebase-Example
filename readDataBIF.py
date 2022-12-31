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

myObj = db.child("BryanKeyTest2").get()

print(myObj.val())
