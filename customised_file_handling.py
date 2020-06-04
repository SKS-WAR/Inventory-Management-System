# -*- coding: utf-8 -*-

import os
import csv
from tempfile import NamedTemporaryFile
import shutil

try:
    os.makedirs("./storage/")
except:
    pass


import db_handler

db_handler.add("sks",price='50',quantity=0)