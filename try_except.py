#asking python to execute a command which may throw a traceback error
try:
    num = int(input("Enter a number: "))
#if traceback error is found it executes the except block 
except:
    num = -1
if num > 0:
    print("Entered a number")
else:
    print("not a number")