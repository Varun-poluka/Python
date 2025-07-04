string1 = input("enter the first string:")
string2 = input("enter the second string:")
# comparision operators can be used on strings too
if string1 < string2:
    print(f"{string1} comes before {string2}")
elif string1 > string2:
    print(f"{string1} comes after {string2}")
else:
    print(f"{string1} is equal to {string2}")