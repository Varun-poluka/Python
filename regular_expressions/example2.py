import re

with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        if re.search("^X-\S+:" , line): # starting with X followed by - with and has 1 or more non whitespace charecters
            print(line)