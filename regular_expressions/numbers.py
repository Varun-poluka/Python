import re

numbers = list() # creating a list to store all numbers
with open("regex_sum_2250374.txt" , "r") as file:
    for line in file:
        line = line.rstrip()
        number = re.findall("[0-9]+" , line) # finding all digits and many more
        if len(number) > 0: # if the returned list is not empty 
            # converting all strings into integers
            for i in range(len(number)):
                number[i] = int(number[i])
                numbers.append(number[i]) # appending each ineteger to list of all numbers
print(sum(numbers)) # finding the sum
