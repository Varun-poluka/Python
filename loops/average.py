sum = 0
count = int(input("enter the number of numbers:"))
for _ in range(count): # iterating count number of times
    n = int(input("enter the number:"))
    sum += n # summing after each number entered
average = sum / count # computing average
print(f"average = {average}")