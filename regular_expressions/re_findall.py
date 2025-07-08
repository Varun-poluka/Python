import re

x = "My 2 favorite numbers are 12 and 29"
y = re.findall("[0-9]+" , x) # combs through the x and return a list of numbers in x 
print(y)

z = re.findall("[aeiou]" , x) # combs through x and return all found vowels in a list
print(z)

a = "From: using the: charecters"
b = re.findall("^F.+:" , a) # greedy matching which returns the largest possible string 
print(b)
c = re.findall("^F.+?:" , a) # fixing greedy match by adding ?
print(c)