# -*- coding: utf-8 -*-

from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'storage/vault.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['name', 'desc', 'price', 'quantity']


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
    
def delete(prod_name):
    with open(filename, 'r', encoding='ascii') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        writer = csv.DictWriter(tempfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] != prod_name:
                row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
                writer.writerow(row)
    shutil.move(tempfile.name, filename)

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

def check(prod_name):
    with open(filename, 'r', encoding='ascii') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields,lineterminator = '\n')
        for row in reader:
            if row['name'] == prod_name:
                row = {'name': row['name'], 'desc': row['desc'], 'price': row['price'], 'quantity': row['quantity']}
                print("Found")
                return row
    return "Not Found"








#update('Nikhil',50)
#delete('Nikhil')
#add("something","it is something","500.00","1000")
print(check("something1"))