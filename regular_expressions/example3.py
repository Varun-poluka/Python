import re
#finding addresses of email or website in the file
with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        address = re.findall("\S+@\S+" , line) # start with non blank charecter with @ in middle and end with non blank charecters
        if len(address) > 0:
            print(address)