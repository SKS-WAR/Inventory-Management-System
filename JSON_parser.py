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