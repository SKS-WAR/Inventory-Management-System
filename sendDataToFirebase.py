# -*- coding: utf-8 -*-

try:
    import AdminSDK
except:
    pass
from firebase_admin import db


def sendData(name,desc,price,quantity):
    row = "1"
    ref = db.reference('/IMS')
    users_ref = ref
    users_ref.update({
        row : {
            'name' : name,
            'desc' : desc,
            'price' : price,
            'quantity' : quantity
        }
    })