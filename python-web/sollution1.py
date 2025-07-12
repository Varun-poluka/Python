import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup # type: ignore

url = input("enter the url:") # asking the user for the URL 
html = urllib.request.urlopen(url).read()# opening the url copying into a file and reading the file to give one string
soup = BeautifulSoup(html , "html.parser")# parsing the string using beautiful soup , return a object 

sum = 0
spans = soup("span") # gives a list of spans in the url 
for span in spans:
    sum += int(span.contents[0]) # each span has a number in its contents

print(sum)

#http://py4e-data.dr-chuck.net/comments_2250376.html