dct = dict()
# creating a dictionary using key-value
dct["varun"] = 4
dct["varshini"] = 14
dct["shriyan"] = 29
print(dct)

dct["varun"] += 2 # dict values can be incemented by using key

print(dct)

#alternate method of creating a dict
dct1 = {"varun" : 10 , "varshini" : 12 , "shriyan" : 14}
print(dct1)

for key in dct1: # printing values of dictionary using key and for loop
    print(f"{dct1[key]}")