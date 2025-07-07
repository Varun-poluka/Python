#importing escessary librarier
import qrcode # type: ignore
import os

#using qrcode.make in the library which takes input of the URL
img = qrcode.make("https://learning.edx.org/course/course-v1:HarvardX+CS50+X/block-v1:HarvardX+CS50+X+type@sequential+block@9bbbe42de8fb420c80ff25e398c2fb2a/block-v1:HarvardX+CS50+X+type@vertical+block@4cbe21402bb4419cb06492c88eea7a69")
img.save("QR.jpeg" , "JPEG") # saving the qr with appropriate entension
