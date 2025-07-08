import re
#finding domain addresses of all emails

with open("words.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
# starting with "From: " matching many charecters till @ then extracting consecutive charecters which are non blank 
        domain = re.findall("From: .*@([^ ]*)" , line)
        if len(domain) > 0:
            print(domain)