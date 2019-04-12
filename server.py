import socket
import sys
import base64
import os
import io

HOST = '' #all available interfaces
PORT = 2222

#1. open Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#2. bind to a address and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()

print ('Socket bind complete')

#3. Listen for incoming connections
s.listen(10)
print ('Socket now listening')


#keep talking with the client
while 1:
    #4. Accept connection
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    #5. Read/Send
    """
    " img: 사진, base64(str)
    " len_data: 클라이언트에서 보내는 문자 길이
    " size: 클라이언트에서 받은 문장 길이 저장
    """
    img = ""
    len_data = conn.recv(1024).decode()
    len_data = int(len_data)
    size = 0
    with open('/home/ubuntu/test.png', 'wb') as f:
      try:
         while 1:
            print("reading data")
            data = conn.recv(65536)
            str_data = data.decode()
            print("data")
            print(data)
            f.write(base64.b64decode(data))
            img += data.decode()
            size += len(str_data)
            # 보낸 문자의 길이와 받은 문자의 길이 비교
            if size >= len_data:
                print("finished reading data")
                break
         print(img)
         print(len(img))
         break
      except Exception as e:
         print(e)

conn.close()
s.close()
