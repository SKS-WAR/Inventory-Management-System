# -*- coding: utf-8 -*-

try:
    import AdminSDK
except:
    pass
from firebase_admin import db
import JSON_parser


def sendData(name,date="",price="",quantity=""):
    ref = db.reference('/IMS')
    row = JSON_parser.transaction_count(ref.get())
    users_ref = ref
    users_ref.update({
        row : {
            'name' : name,
            'date' : date,
            'price' : price,
            'quantity' : quantity
        }
    })