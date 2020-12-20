import socket
import time
HOST = '192.168.1.33'
PORT = 11826
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(2)
    s.sendall(b"{'pass':'2020'}")
    print("sent!")
    time.sleep(7)
    data = ""
    while data != b"{'pass':'success'}":
        try:
            data = s.recv(1024)
            print("Recv!", data)
        except:
            print("no data!")
        s.sendall(b"{'pass':'2020'}")
    while True:
        try:
            data = s.recv(1024)
            print("Recv!", data)
        except:
            print("no data!")
        s.sendall(b"{'command':{'device':'12441','command':'turnOn','name':'Bulb'}}")
        print("sent ON!")
        time.sleep(7)
        try:
            data = s.recv(1024)
            print("Recv!", data)
        except:
            print("no data!")
        time.sleep(7)

        s.sendall(b"{'command':{'device':'12441','command':'turnOff','name':'Bulb'}}")
        print("sent!OFF")
        time.sleep(7)
        try:
            data = s.recv(1024)
            print("Recv!", data)
        except:
            print("no data!")
        time.sleep(5)

except KeyboardInterrupt:
    print('End', "!")