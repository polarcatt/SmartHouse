import json

class A():
    def __init__(self):
        self.id = ""
        self.command = ""
        self.name = ""
    def do_nothing(self):
        pass


def getFromStr(s):
    
    t1 = s[1:-1]
    ta = A()
    if t1[:t1.find(':')] == "'command'":
        t1 = t1[t1.find(':')+1:]
        a = json.loads(t1.replace("'",'"'))
        ta.__dict__ = a
        return ta
    if t1[:t1.find(':')] == "'pass'":
        t1 = '{' + t1 + '}'
        a = json.loads(t1.replace("'",'"'))
        if a['pass'] == CODE:
            return 

s = "{'command':{'id':'123','command':'turnOn','name':'Bulb'}}" 
s2 = "{'pass': '2020'}"
ta = getFromStr(s)
print(ta.id, ta.command, ta.name)
ta = getFromStr(s2)
print(ta.id, ta.command, ta.name)
    