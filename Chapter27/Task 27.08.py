# -*- coding: UTF-8 -*-
class course:
    def __init__(self,t,m):
        self.__coursetitle=t
        self.__maxstudents=m
        self.__numberoflessons=0
        self.__courselesson=[]
        self.__courseassessment = assessment

    def addlesson(self,t,d,r):
        self.__numberoflessons+=1
        self.__courseassessment=append(lesson(t,d,r))

    def addassessment(self,t,m):
        self.__courseassessment=assessment(t.m)

    def outputcoursedetail(self):
        print(self.__coursetitle, 'Maxomum number', self.__maxstudents)
        for i in range(self.__numberoflessons):
            print(self.__courselesson[i].outputcoursedetail())
 
class lesson:
    def __init__(self,t,d,r):
        self.__lessontitle=t
        self.__durationminutes=d
        self.__requireslab=r

    def outputlessondetails(self):
    print(self.__lessontitle,'durationminutes',self.__durationminutes,'requireslab',self.__requireslab)

class assessment:
    def __init__(self,t,m):
        self.__assessmenttitle=t

    def outputlessondetails(self):
        print(self.__assessmenttitle)
