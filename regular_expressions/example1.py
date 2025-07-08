import re

with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        if re.search("^X.*:" , line): # starts with X followed by any number of charecters 0 or more times and end with :
            print(line)