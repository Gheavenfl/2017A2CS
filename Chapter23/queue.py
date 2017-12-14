#S3C3 Harvey Op1
#Complete code for stack version 2.5
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
    global endpointer
    startpointer=null
    endpointer=null
    freelistptr=0
    for i in range(0,10):
        list[i].pointer=i+1
    list[9].pointer=null

def inqueue(newitem):
    global freelistptr
    global startpointer
    global endpointer
    if freelistptr!=null:
        newnodeptr=freelistptr
        list[newnodeptr].data=newitem
        freelistptr=list[newnodeptr].pointer
        list[newnodeptr].pointer=null
        if endpointer==null:
            endpointer=newnodeptr
            startpointer=newnodeptr
        else:
            list[endpointer].pointer=newnodeptr
            endpointer=newnodeptr

def dequeue():
    global freelistptr
    global startpointer
    global endpointer
    if startpointer!=null:
        currentptr=startpointer
        startpointer=list[currentptr].pointer
        list[currentptr].pointer=freelistptr
        freelistptr=currentptr
        if startpointer==null:
            endpointer=null

def Output():
    global startpointer
    currentptr=startpointer
    while currentptr!=null:
        print(list[currentptr].data)
        currentptr=list[currentptr].pointer
