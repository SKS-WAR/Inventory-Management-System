# -*- coding: utf-8 -*-
#Importing the required packages
from tempfile import NamedTemporaryFile
import shutil
import csv

#The file name along with the location
filename = 'storage/vault.csv'
#A temtemporary file for conviniet file handling
tempfile = NamedTemporaryFile(mode='w', delete=False)

#The required fields of the database
fields = ['name', 'desc', 'price', 'quantity']

#update function updates the value to the existing value.
#IFF the file exists
def update(prod_name,prod_quantity):
    with open(filename, 'r', encoding='ascii') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        writer = csv.DictWriter(tempfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] == prod_name:
                print('updating row', row['name'])
                row['quantity'] = (str)(((int)(row['quantity']))+prod_quantity)
            row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    
#delete function deletes the values from the database
#IFF the file exists
def delete(prod_name):
    with open(filename, 'r', encoding='ascii') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        writer = csv.DictWriter(tempfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] != prod_name:
                row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
                writer.writerow(row)
    shutil.move(tempfile.name, filename)

#add functions add a new value to the database
#allowed if no prev. values of the exact item exists
def add(prod_name,prod_desc = "",price=0,quantity=0):
    with open(filename, 'r', encoding='ascii') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        writer = csv.DictWriter(tempfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] == prod_name:
                print("Item already exists.")
                return "Already Exists"
            row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
            writer.writerow(row)
        row = {'name': prod_name, 'desc': prod_desc, 'price': price, 'quantity': quantity}
        writer.writerow(row)
    shutil.move(tempfile.name, filename)

#check function check whether a value exists or not 
def check(prod_name):
    with open(filename, 'r', encoding='ascii') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] == prod_name:
                row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
                print("Found")
                return row
    return "Not Found"