string = input("Enter the string:")
lenght = len(string) #find lenght of the entered string
index = 0
while index < lenght: 
    letter = string[index] # each index in the string represents a letter to loop through
    print(f"{index} {letter}")
    index += 1 # incrementing the index
for letter in string: # printing the letter using a for loop
    print(letter)