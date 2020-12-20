import socket

sock = socket.socket()
port = 11705
sock.bind(('192.168.1.62', port))
print("started!")
sock.listen(10)
con, addr = sock.accept()
print(con, addr)
data = "1"
while data:
	print("waiting")
	data = con.recv(1024)
	print(data.decode().strip())
	con.sendall(b"HELLO GO V TANKI")
sock.close()