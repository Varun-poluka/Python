lst = [1,45,32,76,89,45,98,100,130,4]
largest = 0
# checking if each number in the list is larger than the largest number till now
for number in lst:
    if number > largest:
        largest = number # updating the largest number
print(f"largest = {largest}")