# -*- coding: utf-8 -*-

def process(ISM_json):    
    for row in ISM_json.items():
        #print(person)
        print("Item number :",end = " ")
        item = row[0]
        values = row[1]
        print(item)
        
        #print(values)
        desc = values['desc']
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
        desc = values['desc']
        name = values['name']
        price = values['price']
        quantity = values['quantity']
        print("Name : ",name)
        print("Description :", desc)
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
    desc = values['desc']
    name = values['name']
    price = values['price']
    quantity = values['quantity']
    formatted = str("\n Name : "+ name + "\n Descrption : " + desc + "\n Price : "+ price
          + "\n Quantity : " + quantity)
    print(formatted)
    return formatted
          