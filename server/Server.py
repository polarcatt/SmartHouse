import socket
import select
import Command
import json

class Server:
    def __init__(self, port, logfile, code, timeout):
        self.port = port
        self.sock = socket.socket()
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(10)
        self.rlist = [self.sock]
        self.wlist = []
        self.timeout = timeout
        self.addresses = {}
        self.queue = {}
        self.logfile = logfile
        self.loggedIn = []
        self.notloggedIn = []
        self.code = code

    def getData(self):
        toread, towrite, exc = select.select(self.rlist, self.wlist, self.rlist, self.timeout)
        coms = []
        for r in toread:
            if r is self.sock:
                conn, addr = r.accept()
                self.logfile.write("New connection from " + str(addr) + "\n")
                self.addresses[conn] = addr
                self.rlist.append(conn)
                self.notloggedIn.append(r)
            else:
                try:
                    strData = ""
                    data = r.recv(1024)
                    strData += data.decode()
                    while strData.count('{') != strData.count('}'):
                        data = r.recv(1024)
                        strData += data.decode()
                    print("Got : ", strData)
                    if data:
                        balanceO = 0
                        balanceC = 0
                        curStr = ""
                        strS = []
                        for c in strData:
                            if c == '{':
                                balanceO += 1
                            if c == '}':
                                balanceC += 1
                            curStr += c
                            if balanceO == balanceC:
                                strS.append(curStr)
                                curStr = ""
                        for strData in strS:
                            com = self.getCommand(r, strData)
                            if com.id == "-1":
                                if r in self.notloggedIn:
                                   self.notloggedIn.remove(r)
                                if r not in self.loggedIn:
                                    self.loggedIn.append(r)
                                self.logfile.write("Client logged: " + str(self.addresses[r]) + "\n")
                            elif com.id == "-2" or com.id == "-3":
                                pass
                            else:
                                if r in self.loggedIn:
                                    self.logfile.write("Command passes: " + str(self.addresses[r]) + " "+ com.id + "\n")
                                    coms.append(com)
                    else:
                        self.remove(r)
                except ConnectionResetError:
                    self.remove(r)

        for w in towrite:
            if len(self.queue[w]) > 0:
                w.sendall(self.queue[w][0])
                self.queue[w].pop(0)
            else:
                self.wlist.remove(w)
                self.queue.pop(w, None)
        for e in exc:
            print("Exception with", e)
            self.remove(e)
        return coms

    def remove(self, r):
        self.logfile.write("Client disconnected: " + str(self.addresses[r]) + "\n")
        self.rlist.remove(r)
        if r in self.wlist:
            self.wlist.remove(r)
            self.queue.pop(r, None)
        if r in self.loggedIn:
            self.loggedIn.remove(r)
        if r in self.notloggedIn:
            self.notloggedIn.remove(r)
        r.close()

    def toAnswer(self, data):
        for command in data:
            client = command[0]
            d = command[1]
            print(client, data)
            if client in self.queue.keys():
                self.queue[client].append(d)
            else:
                self.wlist.append(client)
                self.queue[client] = [d]

    def getCommand(self, client, data):
        com = Command.Command()
        try:
            t1 = data[1:-1]
            if t1[:t1.find(':')] == "'command'":
                t1 = t1[t1.find(':')+1:]
                a = json.loads(t1.replace("'",'"'))
                a['client'] = client
                com.__dict__ = a
                return com
            elif t1[:t1.find(':')] == "'pass'"  :
                t1 = '{' + t1 + '}'
                a = json.loads(t1.replace("'",'"'))
                a['client'] = client
                if a['pass'] == self.code:
                    com.id = "-1"
                    return com
                else:
                    com.id = "-2"
                    return com
            else:
                com.id = "-3"
                return com
        except:
            com.id = "-3"
            return com


