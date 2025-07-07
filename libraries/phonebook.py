import csv

name = input("what is the name:")
number = input("what is the number:")
with open("phonebook.csv" , "a" , newline = "") as file: # open a new file in append mode   
    writer = csv.DictWriter(file , fieldnames = ["Name" , "Number"]) # using dictwriter to file and defining different fields or columns
    writer.writerow({"Name" : name , "Number": number}) # writing wrt each fieldname