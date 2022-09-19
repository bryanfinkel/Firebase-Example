import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDsKKzB2iOBeTTF0KsmArPPeWt_CZahty4",
    "authDomain": "crud-python-782a8.firebaseapp.com",
    "projectId": "crud-python-782a8",
    "storageBucket": "crud-python-782a8.appspot.com",
    "messagingSenderId": "449665287559",
    "appId": "1:449665287559:web:36710452f8d11d11c83f22",
    "databaseURL": "https://crud-python-782a8-default-rtdb.firebaseio.com"  # add this config line for database url
}

firebase = pyrebase.initialize_app(firebaseConfig)  # create a firebase app
db = firebase.database()  # get the instance of realtime database using url above

data = {"name": "Ahsan", "age": "22"}  # new object for the unique key we used in createData.py file
db.child("myKey").update(data)  # grab object using "mykey" and then update its data with new object

db.child("myKey").child("name").set("field update")  # we can also set value for a field inside object using set
# function, if key not found in our case "name" then set function create one
