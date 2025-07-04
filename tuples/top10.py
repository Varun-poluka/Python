counts = dict()
# creating a dictionary of all words and count of occurence
with open("words.txt" , "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1

#creating a list of value-key tuples
lst = list()
for key,val in counts.items():
    lst.append((val,key))

#sorting the list based on value
lst = sorted(lst , reverse = True)
#printing the top 10 in the sorted list and print key and value
for val,key in lst[:10]:
    print(key,val)