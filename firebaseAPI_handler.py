# -*- coding: utf-8 -*-


import pyrebase
import JSON_parser


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

db = firebase.database()
user = auth.sign_in_with_email_and_password("sahoosudeep2010@gmail.com", "123456")
try:
    total = db.child('IMS').child('amount').child('total').get(user['idToken']).val()
except :
    total = 0
print(total)
if total == "40":
    users_ref = db.child('IMS').child('amount')
    users_ref.update({"total" : "400"} ,token=user['idToken'])


def login(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Logged in successfully")
        return user
    except :
        print("Unable to login")
        return None
    

def sendProductionData(auth,name,date="",price="",quantity=""):
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child('production').get(auth['idToken']).val())
    except:
        row = "0"
    
    try:
        total = db.child('IMS').child('amount').child('total').get(user['idToken']).val()
    except :
        total = 0
    total = str((int)(quantity) + (int)(total))
    print(total)
    users_ref = db.child('IMS').child('amount')
    users_ref.update({"total" : total} ,token=user['idToken'])
    
    users_ref = db.child('IMS').child('production')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])

def sendDespatchData(auth,name,date="",price="",quantity=""):
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child('despatch').get(auth['idToken']).val())
    except:
        row = "0"
    users_ref = db.child('IMS').child('despatch')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])
    
def amount_calc():
    pass



