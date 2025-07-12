import urllib.request , urllib.parse , urllib.error
import xml.etree.ElementTree as ET

url = input("Enter the url:")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2250378.xml"
file = urllib.request.urlopen(url) # return a file of the url page
data = file.read()# gives one big string of the web page

tree = ET.fromstring(data) # gives back a tree of the XML nodes 
lst = tree.findall(".//count") # finding the tag count and gets list of all nodes 
sum = 0
for item in lst:
    sum += int(item.text)# increasing sum of the contents in the count
    
print(sum)