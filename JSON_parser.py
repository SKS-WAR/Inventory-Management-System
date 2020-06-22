# -*- coding: utf-8 -*-
import datetime
def process(ISM_json):    
    for row in ISM_json.items():
        #print(person)
        print("Item number :",end = " ")
        item = row[0]
        values = row[1]
        print(item)
        
        #print(values)
        date = values['date']
        name = values['name']
        price = values['price']
        quantity = values['quantity']
        print(quantity)
        
def display(ISM_json):    
    for row in ISM_json.items():
        #print(person)
        item = row[0]
        values = row[1]
        print("Item number :", item)
        
        #print(values)
        date = values['date']
        name = values['name']
        price = values['price']
        quantity = values['quantity']
        print("Name : ",name)
        print("Date :", date)
        print("Price :", price)
        print("Quantity :", quantity)
        print("      -------------------")
        
def search(ISM_json,prod_name):    
    for row in ISM_json.items():
        #print(person)
        item = row[0]
        values = row[1]
        if values['name'] == prod_name:
            return format_value(values)
        
def format_value(values):
    date = values['date']
    name = values['name']
    price = values['price']
    quantity = values['quantity']
    formatted = str("\n Name : "+ name + "\n Date : " + date + "\n Price : "+ price
          + "\n Quantity : " + quantity)
    print(formatted)
    return formatted

def transaction_count(ISM_json):
    return len(ISM_json)

def format_to_input():
    pass

def search_by_month(ISM_json,month):
    count = 0
    for row in ISM_json:
        #print(row['date'])
        date = datetime.datetime.strptime(row['date'], "%Y-%m-%d")
        month_name = date.strftime("%B")
        if month == month_name:
            count += 1
    return count