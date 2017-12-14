#S3C3 Harvey Op1
#Complete code for stack version 2

null=-1
class Listnode (object):
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

list=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    list[i]=Listnode('','')

def Initiallist():
    global freelistptr
    global startpointer
    startpointer=null
    freelistptr=0
    for i in range(0,10):
        list[i].pointer=i+1
    list[9].pointer=null

def push(newitem):
    global freelistptr
    global startpointer
    if freelistptr!=null:
        newnodeptr=freelistptr
        freelistptr=list[freelistptr].pointer
        list[newnodeptr].pointer=startpointer
        startpointer=newnodeptr
        list[newnodeptr].data=newitem

def pop():
    global freelistptr
    global startpointer
    if startpointer!=null:
        currentnodeptr=startpointer
        freelistptr=currentnodeptr
        startpointer=list[currentnodeptr].pointer

def Find(item):
    global startpointer
    currentnodeptr=startpointer
    while currentnodeptr!=null and list[currentnodeptr].data<=item:
        if list[currentnodeptr].data==item:
            return currentnodeptr
        else:
            currentnodeptr=list[currentnodeptr].pointer
    return null

def Output():
    global startpointer
    currentptr=startpointer
    while currentptr!=null:
        print(list[currentptr].data)
        currentptr=list[currentptr].pointer
