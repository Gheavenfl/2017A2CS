#S3C3 Harvey Op1
#Binary Tree Version1

null=-1
class Listnode (object):
    def __init__(self, data, leftpointer, rightpointer):
        self.data = data
        self.leftpointer=leftpointer
        self.rightpointer=rightpointer

list=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    list[i]=Listnode('','','')

def Initialise():
    global freelistptr
    global startptr
    freelistptr=0
    startptr=null
    for i in range(10):
        if i<9:
            list[i].leftpointer=i+1
        elif i==10:
            list[i].leftpointer=null
        list[i].rightpointer=null

def Insert(newitem):
    global freelistptr
    global startptr
    if freelistptr!=null:
        currentlistptr=freelistptr
        list[currentlistptr].data=newitem
        freelistptr=list[freelistptr].leftpointer
        list[currentlistptr].leftpointer=null
        list[currentlistptr].rightpointer=null
        if startptr==null:
            startptr=currentlistptr
        else:
            position=startptr
            while position!=null:
                if list[position].data<newitem:
                    previousnode=position
                    list[position].rightpointer
                    position=list[position].rightpointer
                    turn=1
                elif list[position].data>newitem:
                    previousnode=position
                    position=list[position].leftpointer
                    turn=0
            if turn==0:
                list[previousnode].leftpointer=currentlistptr
            else:
                list[previousnode].rightpointer=currentlistptr

def Find(item):
    global startptr
    currentnodeptr=startptr
    while currentnodeptr!=null and list[currentnodeptr].data!=item:
        if list[currentnodeptr].data>item:
            currentnodeptr=list[currentnodeptr].leftpointer
        elif list[currentnodeptr].data<item:
            currentnodeptr=list[currentnodeptr].rightpointer
    if list[currentnodeptr].data!=item:
        return null
    else:
        return currentnodeptr
