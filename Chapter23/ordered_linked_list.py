#Harvey S3C3 Op1
#Final Version

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

def Insertnode(newitem):
    global freelistptr
    global startpointer
    if freelistptr!=null:
        newnodeptr=freelistptr
        list[newnodeptr].data=newitem
        previousnodeptr=null
        freelistptr=list[freelistptr].pointer
        thisnodeptr=startpointer
        while thisnodeptr!=null and list[thisnodeptr].data<newitem:
            previousnodeptr=thisnodeptr
            thisnodeptr=list[thisnodeptr].pointer
        if previousnodeptr==null:
            list[newnodeptr].pointer=startpointer
            startpointer=newnodeptr
        else:
            list[newnodeptr].pointer=list[previousnodeptr].pointer
            list[previousnodeptr].pointer=newnodeptr

def Find(item):
    global startpointer
    currentnodeptr=startpointer
    while currentnodeptr!=null and list[currentnodeptr].data<=item:
        if list[currentnodeptr].data==item:
            return currentnodeptr
        else:
            currentnodeptr=list[currentnodeptr].pointer
    return null

def Delete(item):
    global freelistptr
    global startpointer
    thisnodeptr=startpointer
    while thisnodeptr!=null and list[thisnodeptr].data!=item:
        previousnodeptr=thisnodeptr
        thisnodeptr=list[thisnodeptr].pointer
    if thisnodeptr!=null:
        if thisnodeptr==startpointer:
            startpointer=list[startpointer].pointer
        else:
            list[previousnodeptr].pointer=list[thisnodeptr].pointer
        list[thisnodeptr].pointer=freelistptr
        freelistptr=thisnodeptr

        
def Output():
    global startpointer
    currentptr=startpointer
    while currentptr!=null:
        print(list[currentptr].data)
        currentptr=list[currentptr].pointer

