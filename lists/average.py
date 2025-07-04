lst = list()
# creating a new list
while True:
    inp = input("enter a number:")
    if inp == "done":
        break
    value = float(inp)
    lst.append(value)
average = sum(lst) / len(lst) # sum and len work on list too for computing average
print(f"average = {average}")