file_name = "words1.txt"
# converting all lines in a file to uppercase and printing it
with open (file_name , "r") as file:
    for line in file:
        line = line.upper().strip()
        print(line)