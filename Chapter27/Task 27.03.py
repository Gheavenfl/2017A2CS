import datetime
class libraryitem:
    def __init__ (self, t, a, i):
        self.__title = t
        self.__author__artist = a
        self.__itemid = i
        self.__onloan = False
        self.__duedate = datetime.date.today()

    def gettitle (self):
        return (self.__title)

    def borrowing(self):
        self.__onloan = True
        self.__duedate = self.__duedate + datetime.timedelta(weeks=3)

    def returning(self):
        self.__onloan = False

    def printdetails (self):
        print (self.__title,'; ' ,self.__author__artist,';')
        print (self.__itemid,';', self.__onloan,';', self.__duedate)

class borrowername:
    def __init__(self):
        self.__borrowername=''
        self.__emailaddress=''
        self.__borrowerid=0
        self.__itemsonloan=0

    def constructor(self):
        self.__itemsonloan=0

    def getborrowername(self):
        return self.__borrowername

    def getemailadress(self):
        return self.__emailaddress

    def getborrowerid(self):
        return self.__borrowerid

    def getitemsonloan(self):
        return self.__itemsonloan

    def updateitemsonloan(self,number):
        self.__itemsonloan+=number


    def printdetails(self):
        print (self.__borrowername,';', self.__emailaddress,';')
        print （self.__borrowerid,';', self.__itemsonloan,';')
               
class book(libraryitem):
    def __init__(self, t, a, i):
            libraryitem.__init__(self, t, a, i )
            self.__isrequested = False
            self.__requestedby = O
               
    def getisrequested(self):
            return (self.__isrequested)
               
    def setisrequested(self):
            self.__isrequested = True
               
class cd(libraryitem):
    def __init__ (self, t, a, i):
            libraryitem.__init__ (self, t, a, i)
            self.__genre= ""
               
    def getgenre (self):
            return (self.__genre)
    
    def setgenre (self,g):
            self.__genre=g


xxx=cd("And Justice For All","Metallica","xxx")
sss=cd("Dark Side of the Moon","Pink Floyd","sss")
iii=cd("Black Sabbath","Black Sabbath","iii")
aaa=cd("Silly Love Songs","Paul Mccartny","aaa")
zzz=cd("The Letter","The Box Tops","zzz")
w=libraryitem('a','s','t')

xxx.printdetails()







