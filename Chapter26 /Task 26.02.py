#Task 26.02
#S3C3 Harvey
import pickle

class CAR(object):
    def __init__(self,ID,date,insure,owner):
        self.ID=ID
        self.date=date
        self.insure=insure
        self.owner=owner

def Hash(object):
    s=0
    for i in range(len(object)):
        s=s+int(object[i])
        s=s*100
    return s

Car=[CAR('1354328',2017,'covered','daniel'),CAR('1860012',2014,'covered','kevin'),CAR('1370105',2011,'uncovered','john'),CAR('1870130',2018,'covered','Harvey'),CAR('1820993',2009,'covered','rex')]

Carfile=open('Cars.DAT','wb')
for i in range(5):
    Address = Hash(Car[i].ID)
    Carfile.seek(Address)
    pickle.dump (Car[i], Carfile)
Carfile.close()

Carfile=open('Cars.DAT','rb')
ID=str(input('key in the ID of the car you wish to find'))
address=Hash(ID)
Carfile.seek(address)
ThisCar=pickle.load(Carfile)
print (ThisCar.ID,ThisCar.date,ThisCar.insure,ThisCar.owner)
Carfile.close()

     
     







