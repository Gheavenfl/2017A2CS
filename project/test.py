# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
from sys import exit
import math
import pygame
from pygame.locals import *
import gameobjects
from gameobjects.vector2 import Vector2
import time
central=Vector2(540,370)


n=[540, 70, 690, 110, 799, 219, 840, 370, 799, 520, 690, 629, 540, 670, 390, 629, 280, 520, 240, 370, 280, 220, 389, 110, 539, 70]

def seconddisplay(X,Y):
    a=len(Y)
    s=math.pi/30
    sy=int(central.y-300*math.cos(X*s))
    sx=int(300*math.sin(X*s)+central.x)
    if Y[0]==sx and Y[1]==sy:
        return Y[0:2]
    if a==2:
        if Y[0]!=sx or Y[1]!=sy:
            return
    else:
        return seconddisplay(X,Y[2:])

i=0
while i<=60:
    print(seconddisplay(i,n))
    i+=1

class time(object):# To keep track of time itself
    def __init__(self):
        self.sec=15
        self.min=10
        self.hour=10
        self.daynight=0
        self.day=Day[14].date
    
    def addtime(self):
        if self.sec>59:
            self.sec=0
            self.min+=1
        if self.sec<0:
            self.sec=59
            self.min-=1
        if self.min>59:
            self.min=0
            self.hour+=1
        if self.min<0:
            self.min=59
            self.hour-=1
        if self.hour>11:
            self.hour=0
            if self.daynight==0:
                self.daynight=1
            else:
                self.daynight=0
                self.day=Day[Day[self.day-1].rpointer].date
        if self.hour==-1:
            self.hour=11
            if self.daynight==0:
                self.day=Day[Day[self.day-1].lpointer].date
            self.daynight=1-self.daynight

