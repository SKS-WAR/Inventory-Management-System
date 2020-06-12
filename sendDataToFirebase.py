# -*- coding: utf-8 -*-

try:
    import AdminSDK
except:
    pass
from firebase_admin import db
import JSON_parser


def sendProductionData(name,date="",price="",quantity=""):
    ref = db.reference('/IMS/production/')
    try:
        row = JSON_parser.transaction_count(ref.get())
    except:
        row = "0"
    users_ref = ref
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    })

def sendDespatchData(name,date="",price="",quantity=""):
    ref = db.reference('/IMS/despatch/')
    try:
        row = JSON_parser.transaction_count(ref.get())
    except:
        row = "0"
    users_ref = ref
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    })