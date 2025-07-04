lst = ["hello" , "4" , "9.08"] #creating a list 
for _ in lst: #iterating through a list
    print(f"{_}")

for i in range(len(lst)): # range return a list and len returns lenght of list
    print(lst[i]) # printing a list using indexing 

# changing a element in a list in a index
exchange = input("enter the thing to replace:")
index = int(input("enter the index to exchange:"))
lst[index] = exchange
for _ in lst:
    print(f"{_}")