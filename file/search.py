file_name = "words.txt"
with open(file_name , "r") as file:
    for line in file:
        line = line.rstrip() # removing new line charecter
        #using startswith method of string search for line with From: in the start
        if line.startswith("From:"): 
            print(line)