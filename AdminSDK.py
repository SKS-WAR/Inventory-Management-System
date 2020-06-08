# -*- coding: utf-8 -*-

#importing the required packages
import firebase_admin
from firebase_admin import credentials

#defining and calling the credentials
cred = credentials.Certificate("D:\DontTouch\spesina-b1bcd-firebase-adminsdk-msfs9-1e243cb7d1.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://spesina-b1bcd.firebaseio.com/'})
