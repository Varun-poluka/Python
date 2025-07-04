count = 0
with open("words.txt" , "r") as file: # opening the file as file
    for line in file:
        line = line.rstrip()
        if line.startswith("From:"): # finding a line starting with from:
            count += 1 # tracking the count of lines found
            lsplit = line.split() # spliting the line into strings
            print(lsplit[1]) # printing the second strings 
print(f"{count} lines were found")
