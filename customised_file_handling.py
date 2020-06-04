# -*- coding: utf-8 -*-

import os
import csv
from tempfile import NamedTemporaryFile
import shutil

#try:
    #os.makedirs("./storage/")
#except:
    #pass

filename = "vault.csv"
tempfile = NamedTemporaryFile(mode='w', delete=False)


########################################################################
mydict =[{'name': 'Nikhil','desc': 'COE', 'price': '9.0',  'quantity': '2'}, 
         {'name': 'Sanchit','desc': 'COE', 'price': '9.1',  'quantity': '2'}, 
         { 'name': 'Aditya','desc': 'IT', 'price': '9.3', 'quantity': '2'}, 
         {'name': 'Sagar','desc': 'SE', 'price': '9.5',  'quantity': '1'}, 
         {'name': 'Prateek','desc': 'MCE', 'price': '7.8',  'quantity': '3'}, 
         {'name': 'Sahil','desc': 'EP', 'price': '9.1',  'quantity': '2'}]
# field names
fields = ['name', 'desc', 'price', 'quantity']
# writing to csv file 
with open(filename, 'a') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields,lineterminator = '\n') 
      
    # writing headers (field names) 
    writer.writeheader() 
      
    # writing data rows 
    writer.writerows(mydict) 
    
    
    
########################################################################
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
try :
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
          
        # extracting field names through first row 
        fields = next(csvreader) 
          
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
          
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 
except :
    print("File is not created")
    

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
    # parsing each column of a row 
    for col in row: 
        print("%10s"%col), 
    print('\n')
    