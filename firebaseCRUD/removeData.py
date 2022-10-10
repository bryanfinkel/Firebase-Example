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

db.child("myKey").child("name").remove()  # we can also delete value/whole object by specifying path to that prop in key

