import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup # type: ignore

url = input("enter the url:")
count = int(input("Enter count:"))
position = int(input("enter position:"))
print(url)
while (count > 0):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html , "html.parser")

    tags = soup("a")
    print(tags[position-1].get("href" , None))
    url = tags[position-1].get("href" , None)
    count -= 1

        


