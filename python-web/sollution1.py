import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup # type: ignore

url = input("enter the url:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html , "html.parser")

sum = 0
spans = soup("span")
for span in spans:
    sum += int(span.contents[0])

print(sum)