# -*- coding: utf-8 -*-

import connector
import JSON_parser

from firebase_admin import db

ref = db.reference('/')
print(ref.get())


