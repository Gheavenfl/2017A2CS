#CAR FILE
#S3C3 Harvey
import pickle

class CAR(object):
    def __init__(self):
        self.model='911'
        self.date='2018/12/2'
        self.insure='covered'
        self.owner='unknow'

Thiscar= CAR()
Car=[Thiscar for i in range(5)]
Carfile=open('Cars.DAT','wb')
for i in range(5):
    pickle.dump(Car[i],Carfile)
Carfile.close()


Car2=[]
Carfile=open('Cars.DAT','rb')
for i in range(5):
    Car2.append(pickle.load(Carfile))
Carfile.close()
for i in range(5):
    print (Car2[i].model,Car2[i].date,Car2[i].insure)









