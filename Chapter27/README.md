# Chapter 27 EOF Questions

## |-------Bank account------|

## |----Personalaccount------|  |-----Savingaccount-----|


'''python

    class bankaccount:
        def __init__(self):
            accountholdername=''
            iban=''
        
        def createnewaccount(self,n,i):
            accountholdername=n
            iban=i
        
        def setaccountholdername(self,n):
            accountholdername=n
    
        def getaccountholdername(self):
            return self.accountholdername
        
        def getiban(self):
            return self.iban
        
'''

## Personalaccount
attributes
overdraw
limit
ifoverdrawed



## savingsaccount
attributes
Balance
agreed balance rate

The design is that the class's attributes can be automatically passed into its functions.


## 2.a

SEASON TICKET HOLDER
attributes:
holderemailaddress: STRING
functions:
getaccountholdername()
getholderemailaddress()
setaccountholdername()
setholderemailaddress()

PAY AS YOU GO TICKET HOLDER
attributes:
moneyleft:INTEGER
functions:
getmoneyleft()
addmonryleft()

ContractTicketHolder
attributes:
feepermonth:INTEGER
didcustomerpay:BOOLEAN
functions:
getmoneypermonth()
setmoneypermonth()
getcustomerpayment()
setcustomerpayment()

b(1):

Because the attributes can only be defined by the constuctor of itself, so that if there is a mistake, it will be easy to fix.

b(2):

Because the subclasses need to use these functions, they has to consider these functions as their own.

c.

newcustomer=contrstticketcustomer('A.Smith','xyz@abc.cn',10)


## 3.a

Quene class inheretence node classes

b.

    class nodeclass:
        def __init__(self,data):
            self.__data=data
            self.__pointer=-1
        
        def setdata(self,data):
            self.__data=data
    
        def setpointer(self,pointer):
            self.__pointer=pointer
        
        def getdata(self):
            return self.__data
        
        def getpointer(self):
            return self.__pointer
 
 c.
 
    class queueclass:
        def __init__(self):
            self.__head=-1
            self.__tail=-1
            
d.

    def joinnode(self,data):
        queue.append(nodeclass(data))
        if self.head==-1:
            self.head=len(queue)
        self.tale=len(queue)
        
        
        
        
        
        
        
        





    
    
    



















