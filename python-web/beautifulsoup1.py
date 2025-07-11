import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup # type: ignore

url = input("enter the url:")
html = urllib.request.urlopen(url).read() # gives back a huge string with all the data in the web page
soup = BeautifulSoup(html , "html.parser") # parses through and return a object

tags = soup("a") # searching for all the anchor tags
for tag in tags:
    print(tag.get("href" , None)) # iterating through the ancho tags if found print the links
