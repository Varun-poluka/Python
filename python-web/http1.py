import socket # importing the socket library 

#making the socket
mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#connect the socket to a host and port using connect method which takes a tuple input
mysock.connect(("data.pr4e.org" , 80))
# making the request using GET followed by URL followed by end of line and a blank line
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
# send the request through the socket 
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive data upto 512 charecters 
    if len(data) < 1: # no data means enf of file so break 
        break
    print(data.decode() , end="") # print the received data after decoding 

mysock.close() # close the socket 