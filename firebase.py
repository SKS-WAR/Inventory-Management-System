# -*- coding: utf-8 -*-


import pyrebase

config = {
  'apiKey': "AIzaSyD4O8YcABrlEsYzYnEwO9CocUj9OnYak60",
  'authDomain': "spesina-b1bcd.firebaseapp.com",
  'databaseURL': "https://spesina-b1bcd.firebaseio.com",
  'projectId': "spesina-b1bcd",
  'storageBucket': "spesina-b1bcd.appspot.com",
  'messagingSenderId': "324125011109",
  'appId': "1:324125011109:web:441d07e0eb3ba293acb14c"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Logged in successfully")
        return user
    except :
        print("Unable to login")
        return None
    
    
