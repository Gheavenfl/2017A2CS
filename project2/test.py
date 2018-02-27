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
pygame.init()
screen = pygame.display.set_mode((1080, 900), 0, 32)
clock = pygame.time.Clock()
colorpattern=['color0','color0','color0','color0','color0']
SCREEN_SIZE = (1080,900)
font1 = pygame.font.SysFont('arial', 50)
central=Vector2(540,370)
#file1 = pygame.image.load("Rolex_logo.jpeg").convert()
n=[540, 70, 690, 110, 799, 219, 840, 370, 799, 520, 690, 629, 540, 670, 390, 629, 280, 520, 240, 370, 280, 220, 389, 110, 539, 70]

def seconddisplay(X,Y):#To cauculate when should the mark change color due to the arrival of second
    a=len(Y)
    s=math.pi/30
    sy=int(central.y-300*math.cos(X*s))
    sx=int(300*math.sin(X*s)+central.x)
    if Y[0]==sx and Y[1]==sy:
        return Y[0:2]
    if a==2:
        if Y[0]!=sx or Y[1]!=sy:
            return [0,0]
    else:
        return seconddisplay(X,Y[2:])

def getpos(sec,min,hour):#To get the postion of hour, minute, second hand of the clock
    global central
    s=math.pi/30
    m=math.pi/360
    h=math.pi/6
    e=math.pi/1800
    sy=int(central.y-220*math.cos(sec*s))
    sx=int(220*math.sin(sec*s)+central.x)
    my=int(central.y-(150*math.cos(min*s+sec*e)))
    mx=int(150*math.sin(min*s+sec*e)+central.x)
    hy=int(central.y-(100*math.cos(hour*h+min*m)))
    hx=int(100*math.sin(hour*h+min*m)+central.x)
    return sx,sy,mx,my,hx,hy

class daylist(object):
    def __init__(self,date,lpointer,rpointer):
        self.date=date
        self.lpointer=lpointer
        self.rpointer=rpointer

Day=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(31):
    Day[i]=daylist(i+1,i-1,i+1)
Day[30].rpointer=0
Day[0].lpointer=30

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


class record(object):
    def __init__(self):
        self.sec=0
        self.min=0
        self.hour=0
        self.daynight=0
        self.color=(176,196,222)
    
    def addtime(self):
        if self.sec>=60:
            self.sec=0
            self.min+=1
        if self.min>=60:
            self.min=0
            self.hour+=1

def colorchange(self):
    if colorchange==True:
        self.color=(112,128,144)


c=time()
alarm=record()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()
    screen.fill([176,196,222])
    text = font1.render(str(c.day),True,(255,255,255))
    display= font1.render(("am"),True,(255,255,255))
    displayy= font1.render(("pm"),True,(255,255,255))
    c.addtime()
    c.sec+=1# add up one second each loop
    seconddisplay(c.sec,n)
    sx,sy,mx,my,hx,hy=getpos(c.sec,c.min,c.hour)
    clock.tick(10)# set the frequency
    pygame.draw.line(screen,(138,43,226),central,(mx,my),20)
    pygame.draw.line(screen,(138,43,226),central,(hx,hy),30)
    pygame.draw.circle(screen,(255,218,185),(mx,my),20)
    pygame.draw.circle(screen,(255,218,185),(hx,hy),20)
    pygame.draw.circle(screen,(138,43,226),(540,370),16)
    pygame.draw.circle(screen,(138,43,226),((540, 70)),14)
    pygame.draw.circle(screen,(138,43,226),((690, 110)),14)
    pygame.draw.circle(screen,(138,43,226),((799, 219)),14)
    pygame.draw.circle(screen,(138,43,226),((840, 370)),14)
    pygame.draw.circle(screen,(138,43,226),(799, 520),14)
    pygame.draw.circle(screen,(138,43,226),(690, 629),14)
    pygame.draw.circle(screen,(138,43,226),(540, 670),14)
    pygame.draw.circle(screen,(138,43,226),(390, 629),14)
    pygame.draw.circle(screen,(138,43,226),(280, 520),14)
    pygame.draw.circle(screen,(138,43,226),(240, 370),14)
    pygame.draw.circle(screen,(138,43,226),(280, 220),14)
    pygame.draw.circle(screen,(138,43,226),(389, 110),14)
    # screen.blit(file1,(540,200))
    tx,ty=seconddisplay(c.sec,n)
    if tx+ty!=0:#determine whether to change a mark's color
        pygame.draw.circle(screen,(255,218,185),seconddisplay(c.sec,n),14)
    if c.daynight==0:
        screen.blit(display,(470,400))
    if c.daynight==1:
        screen.blit(displayy,(470,400))
    screen.blit(text,(570,400))
    pygame.display.update()

