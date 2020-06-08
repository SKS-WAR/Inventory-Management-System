# -*- coding: utf-8 -*-
#importing the AdminSDK
try:
    import AdminSDK
except:
    pass
from firebase_admin import db

ref = db.reference('/')
print(ref.get())
