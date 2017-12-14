#S3C3 Harvey OP1
#Dictionary Version 1

class Listnode (object):
    def __init__(self, key, data):
        self.key = key
        self.data = data

list=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    list[i]=Listnode(None,None)

def Hash(item):
    Key=0
    for i in range(len(item)):
        if item[i].lower()==item[i] and item[i]!=' ':
            Key+=1
    Key=Key%10
    return Key

def Insert(key,data):
    Index=Hash(key)
    while list[Index].data!=None:
        Index+=1
        if Index>9:
            Index=0
    list[Index].key=key
    list[Index].data=data

def Find(key):
    Index=Hash(key)
    loop=0
    while list[Index].key!=key and list[Index].data!=None:
        if Index>9:
            Index=0
            loop+=1
        elif Index<9:
            Index+=1
        if loop>1:
            break
    if list[Index].key==key:
        return Index



Hash(
