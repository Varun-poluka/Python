# couting in a dictionary using the get method
counts = dict()
names = ["shriyan","varun","varun","shriyan","varshini","varun"]
for name in names: #iterating through all the names in the list
    counts[name] = counts.get(name , 0) + 1 # get method checks the name in the dict and return second if not found
print(counts)