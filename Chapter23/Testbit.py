#Testbit version1

def Testbit(field, bit):
    test=2**bit
    if field&bit==bit:
        print 'True'
    else:
        print 'false'

field=input('please enter your test field')
bit=input('please enter your test field')
Testbit(field, bit)
