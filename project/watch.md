# Christmas Project

I always wanted to purchase a watch

so I decided to make a watch using pygame

since pygame refresh at a constant rate, I can take advantage of that.

I can either get the initial time from the computer, or input them manually.

The watch should include a date function, and a display of am/pm.

The display of each hand of second/hour/minute should include two positions.

The of the central point of the watch, the other point should be calculated 

using a function that uses the time record kept inside the program.I think I

can somehow use recursion and linked list.

The Watch uses math equations to calculate the relative position of the hands on the clock

## def getpos(sec,min,hour):#To get the postion of hour, minute, second hand of the clock
## s=math.pi/30
## m=math.pi/360
## h=math.pi/6
## e=math.pi/1800
## sy=int(central.y-220*math.cos(sec*s))
## sx=int(220*math.sin(sec*s)+central.x)
## my=int(central.y-(150*math.cos(min*s+sec*e)))
## mx=int(150*math.sin(min*s+sec*e)+central.x)
## hy=int(central.y-(100*math.cos(hour*h+min*m)))
## hx=int(100*math.sin(hour*h+min*m)+central.x)
## return sx,sy,mx,my,hx,hy

It uses two classes to record the time itself and the time of the alarm clock

and a function within the clock is there to record the interchange of the time, such as second pass 60, minute pass 60 or hour pass 12

It runs with the initial time fetch from the system clock


## def addtime(self):
## if self.sec>59:
## self.sec=0
## self.min+=1
## if self.sec<0:
## self.sec=59
## self.min-=1
## if self.min>59:
## self.min=0
## self.hour+=1
## if self.min<0:
## self.min=59
## self.hour-=1
## if self.hour>11:
## self.hour=0
## if self.daynight==0:
## self.daynight=1
## else:
## self.daynight=0
## self.day=Day[Day[self.day-1].rpointer].date
## if self.hour==-1:
## self.hour=11
## if self.daynight==0:
## self.day=Day[Day[self.day-1].lpointer].date
## self.daynight=1-self.daynight

It includes an alarm clock system which would play Paul McCartney's  Silly Love Songs






