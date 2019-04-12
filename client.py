#python3

import socket
import base64
import sys
import io
import os
from PIL import Image
from array import array

HOST = '52.78.219.61'
PORT = 3078
#HOST = '3.18.202.129'
#PORT = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# image read
img = open('home.png',"rb")

b = base64.b64encode(img.read())
size= str(len(b))

# send size of string
s.send(size.encode('utf-8'))

# send image_str
s.sendall(b)

img.close()

data = s.recv(65536)
print ('result: ' + data.decode())

s.close()