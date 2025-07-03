lst = [1,45,32,76,89,45,98,100,130,4]
smallest = None
for i in lst: # iterating through each number in the list
    if smallest is None: # if first iteration set smallest to first number
        smallest = i
    elif i < smallest: # checking if number is smaller than the smallest before
        smallest = i # updating the smallest number
print(f"smallest = {smallest}")
