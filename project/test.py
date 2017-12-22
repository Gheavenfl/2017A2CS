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

