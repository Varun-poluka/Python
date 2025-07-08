import re # import regular expressions library

with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        if re.search("^From:" , line): #searching for From: in the begining of each line (works like startswith())
            print(line)
# ^ regex searched for the string after ^ in the begining of specified string