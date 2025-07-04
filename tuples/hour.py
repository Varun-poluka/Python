#printing each hour in time when the mail was sent and how many times
counts = dict()
with open("words.txt" , "r") as file:
    for line in file:
        line.rstrip()
        if line.startswith("From"):
            words = line.split() # spliting the line into words
            if words[0] == "From": # taling the time 
                time = words[5].split(":") # spliting the time with reference to :
                counts[time[0]] = counts.get(time[0] , 0) + 1 # creating a dict of hour and occurence
lst = sorted(counts.items()) # sorted based on key
for k,v in lst:
    print(k , v)
