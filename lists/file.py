mlist = list()
with open("romeo.txt" , "r") as file: # opening a file in read mode
    for line in file:
        line = line.rstrip()
        lsplit = line.split() # for each line in the file split it into a list of strings
        for word in lsplit:
            if word not in mlist:
                mlist.append(word) # adding the words to the main list if word is not there
mlist.sort() # sorting the list of words in the file 
print(mlist)