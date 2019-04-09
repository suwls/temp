import socket
s = socket.socket()
host = socket.gethostname()
port = 3078
s.bind((host, port))
s.listen(5)
while True:
	c.addr = s.addr()
	print('Got connection from',addr)
	c.send(b'Thank you for connecting')
	c.close()