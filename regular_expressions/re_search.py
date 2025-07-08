import re # importing the regular expressions library 

with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        if re.search("From:" , line): # using re.search to search for from in each line
            print(line)
#did not use any regex so it functions same as find and print all the lines which have from regardless of position