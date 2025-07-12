import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup # type: ignore

url = input("enter the url:")# asking user for the url 
count = int(input("Enter count:")) # asking the use the number of pages to open
position = int(input("enter position:")) # asking the user of position of link in each page 
print(url)
while (count > 0): # looping for the number of time pages should be open
    html = urllib.request.urlopen(url).read()# getting the contents of the page as one big string
    soup = BeautifulSoup(html , "html.parser") # parsing the html file

    tags = soup("a") # searching a anchor tags in the page and getting a list
    print(tags[position-1].get("href" , None)) # printing the url in the position 
    url = tags[position-1].get("href" , None) # updating the url to the url in the position to open it 
    count -= 1

#http://py4e-data.dr-chuck.net/known_by_Suhaira.html
