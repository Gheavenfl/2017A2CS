#S3C3 Harvey Op1
#Complete code for Alarm version 2.5
# input 0 for button, 1 for sensor, 2 for pin

import time
def Initialize():
    global alarm
    global State
    alarm=0
    State=0

def inputing():
    global State
    global alarm
    item=str(input('input'))
    if item=='button':
        State=1
    if State=:
        if item==1:
            alarm=1
    elif State==0:
        if item==1:
            alarm=0
    if item==2:
        State=0
        alarm=0

def ring():
    global alarm
    if alarm==1:
        print("alarm")

Initialize()
print("input 0 for button, 1 for sensor, 2 for pin")
while 1:
    inputing()
    ring()







