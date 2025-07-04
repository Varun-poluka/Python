str1 = input("Enter the string:")
search = input("Enter the sequence to be searched:")
#find method takes a parameter and searches the string and returns the index
print(f"{search} is in the {str1.find(search)} index of {str1}")
#upper method converts the whole string to uppercase
print(f"{str1} in uppercase is {str1.upper()}")
#lower method converts the whole string to lowercase
print(f"{str1} in lowercase is {str1.lower()}")
#capitalize method converts first letter of the string to capital letter
print(f"First letter capitalised is {str1.capitalize()}")
replace = input("enter the sequnce to replace:")
what = input("enter the sequence to be replaced:")
#replace takes in two parameter what to replace and with what and return the replaces string
new_str = str1.replace(replace , what)
print(f"new string is {new_str}")
str2 = input("enter a string with whitespaces on both sides:")
#rstrp removes all whitespaces to right side
str3 = str2.rstrip()
#lstrip removes all whitespaces to left side
str4 = str2.lstrip()
#strp removes all the whitespaces in a string
str5 = str2.strip()
print(f"{str2} without right sided whitespaces is {str3}")
print(f"{str2} without left sided whitespcaes is {str4}")
print(f"{str2} with no whitespces at all is {str5}")
line = input("enter a line:")
start = input("enter a word to search the line:")
# startswith checks if the parameter is present in the string
if line.startswith(start) == True:
    print("Yes")
else:
    print("No")