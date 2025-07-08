import re
#printing only email from the file
with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
# find all lines with start with From: and have non whitespace on both sides with an @ in the middle 
        email = re.findall("^From: (\S+@\S+)" , line)
        if len(email) > 0:
            print((email))