# prompt the user for input until done is entered
while True:
    n = input("enter:")
    if n[0] == '#':
        continue #if first charecter of the string is # then move to next iteration
    if n == "done":
        break #if striing is done then break out of the loop
    print(n) #print everything entered if it does not start with #
print("done")
