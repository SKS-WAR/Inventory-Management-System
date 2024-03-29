# -*- coding: utf-8 -*-


import pyrebase
import JSON_parser


config = {}  //paste your config here

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

db = firebase.database()
user = auth.sign_in_with_email_and_password("sahoosudeep2010@gmail.com", "123456")
try:
    total = db.child('IMS').child('amount').child('total').get(user['idToken']).val()
except :
    total = 0
#print(total)
if total == "40":
    users_ref = db.child('IMS').child('amount')
    users_ref.update({"total" : "400"} ,token=user['idToken'])
json = db.child('IMS').child('despatch').get(user['idToken']).val()
#print(json)
#print(JSON_parser.search_by_month(json,"January"))


def login(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Logged in successfully")
        return user
    except :
        print("Unable to login")
        return None
    

def sendFilledBottlesProductionData(auth,name,date="",price="",quantity=""):
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child("bottles").child("filledBottles").child('production').get(auth['idToken']).val())
    except:
        row = "0"
    
    try:
        total = db.child('IMS').child("bottles").child("filledBottles").child('amount').child('total').get(user['idToken']).val()
    except :
        total = "0"
    if total == None:
        total = "0"
    total = str((int)(quantity) + (int)(total))
    print(total)
    users_ref = db.child('IMS').child("bottles").child("filledBottles").child('amount')
    users_ref.update({"total" : total} ,token=user['idToken'])
    
    users_ref = db.child('IMS').child("bottles").child("filledBottles").child('production')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])

def sendFilledBottlesDespatchData(auth,name,date="",price="",quantity=""):
    
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child("bottles").child("filledBottles").child('despatch').get(auth['idToken']).val())
    except:
        row = "0"
    
    try:
        total = db.child('IMS').child("bottles").child("filledBottles").child('amount').child('total').get(user['idToken']).val()
    except :
        total = 0
        
    if total == None:
        total = "0"
    total = str((int)(total) - (int)(quantity))
    print(total)
    users_ref = db.child('IMS').child("bottles").child("filledBottles").child('amount')
    users_ref.update({"total" : total} ,token=user['idToken'])
    
    
    users_ref = db.child('IMS').child("bottles").child("filledBottles").child('despatch')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])

def bottlesFilledBottles_calc_month(auth,month):
    #amount = db.child('IMS').child('amount').child('total').get(auth['idToken']).val()
    json = db.child('IMS').child("bottles").child("filledBottles").child('production').get(auth['idToken']).val()
    production_count = JSON_parser.search_by_month(json,month)
    json = db.child('IMS').child("bottles").child("filledBottles").child('despatch').get(auth['idToken']).val()
    despatch_count = JSON_parser.search_by_month(json,month)
    amount = production_count - despatch_count
    return amount,production_count,despatch_count

    
################################################################################################



def sendEmptyBottlesProductionData(auth,name,date="",price="",quantity=""):
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child("bottles").child("emptyBottles").child('production').get(auth['idToken']).val())
    except:
        row = "0"
    
    try:
        total = db.child('IMS').child("bottles").child("emptyBottles").child('amount').child('total').get(user['idToken']).val()
    except :
        total = "0"
    if total == None:
        total = "0"
    total = str((int)(quantity) + (int)(total))
    print(total)
    users_ref = db.child('IMS').child("bottles").child("emptyBottles").child('amount')
    users_ref.update({"total" : total} ,token=user['idToken'])
    
    users_ref = db.child('IMS').child("bottles").child("emptyBottles").child('production')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])

def sendEmptyBottlesDespatchData(auth,name,date="",price="",quantity=""):
    
    try:
        row = JSON_parser.transaction_count(db.child('IMS').child("bottles").child("emptyBottles").child('despatch').get(auth['idToken']).val())
    except:
        row = "0"
    
    try:
        total = db.child('IMS').child("bottles").child("emptyBottles").child('amount').child('total').get(user['idToken']).val()
    except :
        total = 0
        
    if total == None:
        total = "0"
    total = str((int)(total) - (int)(quantity))
    print(total)
    users_ref = db.child('IMS').child("bottles").child("emptyBottles").child('amount')
    users_ref.update({"total" : total} ,token=user['idToken'])
    
    
    users_ref = db.child('IMS').child("bottles").child("emptyBottles").child('despatch')
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    },token=auth['idToken'])

#def amount_calc():
#    pass


def bottlesEmptyBottles_calc_month(auth,month):
    #amount = db.child('IMS').child('amount').child('total').get(auth['idToken']).val()
    json = db.child('IMS').child("bottles").child("emptyBottles").child('production').get(auth['idToken']).val()
    production_count = JSON_parser.search_by_month(json,month)
    json = db.child('IMS').child("bottles").child("emptyBottles").child('despatch').get(auth['idToken']).val()
    despatch_count = JSON_parser.search_by_month(json,month)
    amount = production_count - despatch_count
    return amount,production_count,despatch_count
#something = calc_month(user,"June")
#print(something)
    



#sendProductionData(user,"something","someday","50","500")
