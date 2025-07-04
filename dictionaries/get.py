# couting in a dictionary using the get method
counts = dict()
line = input("Enter a line:") #asks input for a string
words = line.split() # list of words returns from split
for word in words:
    counts[word] = counts.get(word , 0) + 1 # using get function to create dict of words and count
print(counts)