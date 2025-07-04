# couting in a dictionary using the get method
counts = dict()
line = input("Enter a line:") #asks input for a string
words = line.split() # list of words returns from split
for word in words:
    counts[word] = counts.get(word , 0) + 1 # using get function to create dict of words and count
print(counts)
print()

keys = list(counts) #list function return the list of keys from the dictionary
print(keys)
print()
keys = counts.keys() # keys method return a list of dict_keys
print(keys)
print()
values = counts.values() # values method return a list of values in the dictionary
print(values)