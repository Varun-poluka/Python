import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") # gives back a file handle
for line in fhand:
    print(line.decode().rstrip()) # decode and print each line in the file