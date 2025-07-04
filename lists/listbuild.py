# creating a list from scratch
lst = list()
lenght = int(input("enter the lenght of the list:"))
n = 0
while n < lenght:
    element = input(f"Enter the {n} element:")
    lst.append(element) # append is a method which add a new element to end of the list
    n += 1
print(lst)
lst.sort() # sort is a method which lets the list sort itself out 
print(f"sorted list = {lst}")