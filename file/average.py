file_name = "words.txt"
# searching for lines in file and computing the average of numeric codes in the line
count , total = 0 , 0
with open(file_name , "r") as file:
    for line in file:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            count += 1
            start = line.find("0")
            total += float(line[start:])
average = total / count
print(f"{average}")