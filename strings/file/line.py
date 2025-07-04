#print each line in a file
file_name = "romeo.txt"
with open(file_name , "r") as file: # opening the file in reading mode and nameing it file
    for line in file: #iterating through each line in file
        line = line.rstrip() #removing the next line charected at the end
        print(line)