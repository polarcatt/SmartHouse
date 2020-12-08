import socket
import time
HOST = 'localhost'
PORT = 11837
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(0.1)
    i = 1
    #s.sendall(b"{'pass':'2020'}")
    while i < 4:
        s.sendall(b"{'command':{'id':'123','command':'turnOn','name':'Bulb'}}")
        time.sleep(2)
        try:
        	data = s.recv(1024)
        	print("Recv!", data)
        except:
        	print("no data!")
        print("sent!")
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print('End', "!")