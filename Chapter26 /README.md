# Chapter 26 EOF Questions

1.a 1

class CustomerRecord:
def __init__(self):
    self.CustomerID=0
    self.CustomerName=''
    self.TelNumber=''
    self.ValueOfOrders=0
    
CustomerData=[CustomerRecord for i in range(999)]


1.b 1

def Hash(CustomerID):
    Address=CustomerID % 1000
    return Address
    
def AddRecord(CustomerData, Customer):
    i=Hash(Customer.CustomerID)
    while CustomerData[ i ] != '':
        i+=1
    CustomerData[ i ]=cCustomer
    
def FindRecord(CustomerID, CustomerData):
    i=Hash(CustomerID)
    while CustomerData[ i ].ID!=CustomerID:
        i+=1
    return i
    

1.c

import pickle
customerfile=open('CustomerData.DAT','wb')
for i in range(999):
    pickle.dump(CustomerData[i], customerfile)
customerfile.close()


1.d

We should change the program to a simple one that would dump a record to
the file directly as it arrives, we should delete the hashing part of the program.
What's more, the program would access the file in no perticular order


2

Filename=input('input the filename you wish to find:')
Try:
    pickle.seek(Filename)
except:
    print('file does not exist')
    Filename=input('input the filename you wish to find:')
else:
    pickle.seek(Filename)
    file=pickle.load(File)
File.close()

    

























