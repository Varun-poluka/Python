# finding a most occuring word and number of times it comes up 
counts = dict()
with open("words.txt" , "r") as file:
    for line in file:
        words = line.split() # for each line in the file split it into a list of words
        for word in words:
            counts[word] = counts.get(word , 0) + 1 #creating a dict of words and occurence
big_count = None
big_words = None

for word , count in counts.items(): #iterating to each word and count in the list of tuples of dict
    if big_count is None or count > big_count:
        #updating highest count and occuring word
        big_word = word
        big_count = count

print(big_word , big_count)