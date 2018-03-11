# -*- coding: UTF-8 -*-
import datetime
import sys

books=[]
borrowers=[]
cds=[]

class libraryitem:
    def __init__ (self, t, a, i):
        self.__title = t
        self.__author__artist = a
        self.__itemid = i
        self.__onloan = False
        self.__duedate = datetime.date.today()
        self.__borrowerid=''

    def gettitle (self):
        return (self.__title)

    def borrowing(self,id):
        self.__onloan = True
        self.__duedate = self.__duedate + datetime.timedelta(weeks=3)
        self.__borrowerid=id

    def returning(self):
        self.__onloan = False
        self.__borrowerid=''

    def printdetails (self):
        print (self.__title,'; ' ,self.__author__artist,';')
        print (self.__itemid,';', self.__onloan,';', self.__duedate)

class borrower:
    def __init__(self,bn,be,bi,io):
        self.__borrowername=bn
        self.__emailaddress=be
        self.__borrowerid=bi
        self.__itemsonloan=io

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
        print (self.__borrowername,';', self.__emailaddress, ';')
        print (self.__borrowerid,';', self.__itemsonloan, ';')
               
class book(libraryitem):
    def __init__(self, t, a, i):
            libraryitem.__init__(self, t, a, i )
            self.__isrequested = False
            self.__requestedby = ''
               
    def getisrequested(self):
            return (self.__isrequested)
            return (self.__requestedby)
               
    def setisrequested(self,by):
            self.__isrequested = True
            self.__requestedby = by

               
class cd(libraryitem):
    def __init__ (self, t, a, i):
            libraryitem.__init__ (self, t, a, i)
            self.__genre= ""
               
    def getgenre (self):
            return (self.__genre)
    
    def setgenre (self,g):
            self.__genre=g

def library(c):
    global books
    global borrowers
    global cds
    global book
    global cd
    global borrower
    if c==1:
        a=input('enter borrower name')
        b=input('enter borrower email address')
        h=input('enter borrower ID')
        d=input('enter itemsonloan')
        e=borrower(a,b,h,d)
        borrowers=borrowers.append(e)
    if c==2:
        a=input('enter book title')
        b=input('enter writer')
        h=input('enter bookid')
        e=book(a,b,h)
        books=books.append(e)
    if c==3:
        a=input('enter cd name')
        b=input('enter artist')
        h=input('enter cd id')
        g=input('enter genre')
        e=cd(a,b,h)
        e.setgenre(g)
        cds=cds.append(e)
    if c==4:
        a=input('enter book title')
        b=input('enter borrower name')
        b.updateitemsonloan(self,1)
        a.borrowing(b.getborrowerid())
    if c==5:
        a=input('enter book title')
        b=input('enter borrower name')
        b.updateitemsonloan(self,-1)
        a.returning(b.getborrowerid())
    if c==6:
        a=input('enter cd title')
        b=input('enter borrower name')
        b.updateitemsonloan(self,1)
        a.borrowing(b.getborrowerid())
    if c==7:
        a=input('enter cd title')
        b=input('enter borrower name')
        b.updateitemsonloan(self,-1)
        a.returning(b.getborrowerid())
    if c==8:
        a=input('enter book title')
        b=input('enter requester name')
        a.setisrequested(self,b)
    if c==99:
        sys.exit()

while True:
    print('1 - Add a new borrower; 2 - Add a new book; 3 - Add a new CD; 4 - Borrow a book; 5 - Return a book; 6 - Borrow a CD; 7 - Return a CD; 8 - Request book; 9 - Print all details; 99 - Exit program')
    c=input('Enter your menu choice:')
    library(c)










 