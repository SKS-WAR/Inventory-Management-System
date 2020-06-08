# -*- coding: utf-8 -*-

import connector
import JSON_parser

ref = db.reference('/IMS')
#print(ref.get())

JSON_parser.process(ref.get())