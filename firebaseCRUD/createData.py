# Modification Record
# 9-22: Bryan replaced Ahsan's firebase config data block with Bryan's data block

import pyrebase

firebaseConfig = {
    # This is Bryan's config data (Ahsan's data is below)

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

data = {"name": "jerry"}  # create a simple object to store
db.push(data)  # use push method of pyrebase to store data on firebase. it will also create a unique key as well

data = {"name": "John"}  # another simple object to store but this time with our own key
db.child("myKey").set(data)  # use push method of pyrebase to store data on firebase but with "mykey" as unique key
