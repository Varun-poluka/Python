largest = None
smallest = None
while True:
    a = input("enter a number:") # keep asking for input 
    if a == "done": # if input is "done" break out of the loop
        break
    else:
        try:
            a = int(a) # try to convert input to integer
        except:
            print("Invalid input") # if it is not a number then throw error message
            continue
# updating the largest each time we enter a number
    if largest is None:
        largest = a
    else:
        if largest < a:
            largest = a
# updating the smallest each time we enter a number
    if smallest is None:
        smallest = a
    else:
        if smallest > a:
            smallest = a 
print(f"largest = {largest}")
print(f"smallest = {smallest}")