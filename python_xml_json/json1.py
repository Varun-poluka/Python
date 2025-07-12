import urllib.request , urllib.parse , urllib.error
import json

url = input("enter:")
if len(url)< 1:
    url = "http://py4e-data.dr-chuck.net/comments_2250379.json"

file = urllib.request.urlopen(url)
data = file.read()

sum = 0
info = json.loads(data)
for item in info["comments"]:
    sum += int(item["count"])

print(sum)