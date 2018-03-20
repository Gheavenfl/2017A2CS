#S3C3 Harvey Op1
#recursion 1 code

def fact(X):
    if X==1:
        return 1
    else:
        return X*fact(X-1)


def bunnyEars(X):
    if X==0:
        return 0
    else:
        return 2+bunnyEars(X-1)


def fibonacci(X):
    if X==0:
        return 0
    if X==1:
        return 1
    else:
        return fibonacci(X-2)+fibonacci(X-1)


def bunnyEars2(X):
    if X==1:
        return 2
    else:
        if X%2==1:
            return bunnyEars2(X-1)+2
        else:
            return bunnyEars2(X-1)+3


def trangle(X):
    if X==0:
        return 0
    else:
        return X+trangle(X-1)


def sumdigits(X):
    if X==0:
        return 0
    else:
        return X%10+sumdigits(X/10)


def count7(X):
    if X==0:
        return 0
    else:
        if X%10==7:
            return 1+count7(X/10)
        else:
            return count7(X/10)

def count8(X):
    if X==0:
        return 0
    else:
        if X%10==8:
            return 1+count8(X/10)
        else:
            return count8(X/10)

def powerN(X,Y):
    if Y==0:
        return 1
    else:
        return X * powerN(X,Y-1)

def countx(X):
    a=len(X)
    if X=='':
        return 0
    else:
        if X[a-1]=='x':
            return 1+countx(X[:a-1])
        else:
            return countx(X[:a-1])

def counthi(X):
    a=len(X)
    if a==0 or a==1:
        return 0
    else:
        if X[a-2:]=='hi':
            return 1+counthi(X[:a-1])
        else:
            return counthi(X[:a-1])


def changexy(X):
    a=len(X)
    if a==0:
        return ''
    else:
        if X[a-1]=='x':
            return changexy(X[:a-1])+'y'
        else:
            return changexy(X[:a-1])+X[a-1]


def changepi(X):
    a=len(X)
    if a==0:
        return ''
    else:
        if X[a-2:]=='pi':
            return changepi(X[:a-2])+'3.14'
        else:
            return changepi(X[:a-1])+X[a-1]


def nox(X):
    a=len(X)
    if a==0:
        return ''
    else:
        if X[a-1]=='x':
            return nox(X[:a-1])
        else:
            return nox(X[:a-1])+X[a-1]


def array6(X,I):
    a=len(X)
    if I==a-1 and X[I]!=6:
            return False
    if X[I]==6:
            return True
    else:
            return array6(X,I+1)

def array11(X,I):
    a=len(X)
    if I==a-1 and X[I]!=11:
        return 0
    if X[I]==11:
        return 1 + array11(X,I+1)
    else:
        return array11(X,I+1)


def array220(X,I):
    a=len(X)
    if I>a-2:
        return False
    if X[I+1]==10*X[I]:
        return True
    else:
        return array220(X,I+1)


def allstar(X):
    a=len(X)
    if a==1:
        return X
    else:
        return allstar(X[:a-1])+'*'+X[a-1]


def pairstar(X):
    a=len(X)
    if a==1:
        return X
    if X[a-1]==X[a-2]:
        return pairstar(X[:a-1])+'*'+X[a-1]
    else:
        return pairstar(X[:a-1])+X[a-1]


def endX(X):
    a=0
    if X=='':
        return ''
    if X[a]=='x':
        return endX(X[a+1:])+'x'
    else:
        return X[a]+endX(X[a+1:])


def countpairs(X):
    a=len(X)
    if a<3:
        return 0
    else:
        if X[a-1]==X[a-3]:
            return 1+countpairs(X[:a-1])
        else:
            return countpairs(X[:a-1])


def countABC(X):
    a=len(X)
    if a<3:
        return 0
    else:
        if X[a-1]=='c' and X[a-2]=='b' and X[a-3]=='a':
            return 1+countABC(X[:a-1])
        elif X[a-1]=='a' and X[a-2]=='b' and X[a-3]=='a':
            return 1+countABC(X[:a-1])
        else:
            return  countABC(X[:a-1])


def count11(X):
    a=len(X)
    if a<2:
        return 0
    else:
        if X[a-1]=='1' and X[a-2]=='1':
            return 1+count11(X[:a-2])
        else:
            return count11(X[:a-1])


def stringClean(X):
    a=len(X)
    if a==0:
        return ''
    else:
        if X[a-1]==X[a-2]:
            return stringClean(X[:a-2])+X[a-2]
        else:
            return stringClean(X[:a-1])+X[a-1]


def counthi2(X):
    a=len(X)
    if a<3:
        if X[1]=='i' and X[0]=='h':
            return 1
        else:
            return 0
    else:
        if X[a-1]=='i' and X[a-2]=='h' and X[a-3]!='x':
            return 1+counthi2(X[:a-1])
        else:
            return counthi2(X[:a-1])


def parentbit(X):
    if X=='':
        return ''
    else:
        if X[-1]!=')':
            return parentbit(X[:-1])
        elif X[0]!='(':
            return parentbit(X[1:])
        else:
            return X


def nestparent(X):
    a=len(X)
    if a==0:
        return True
    else:
        if X[0]=='('and X[-1]==')':
            return nestparent(X[1:-1])
        else:
            return False


def strCount(X,Y):
    a=len(X)
    b=len(Y)
    if a<b:
        return 0
    else:
        if X[-b:]==Y:
            return 1+strCount(X[:a-1],Y)
        else:
            return strCount(X[:a-1],Y)


def strCopies(X,Y,N):
    a=len(X)
    b=len(Y)
    if a<b and N==0:
        return True
    if a<b and N>0:
        return False
    else:
        if X[-b:]==Y:
            return strCopies(X[:a-1],Y,N-1)
        else:
            return strCopies(X[:a-1],Y,N)

def strDist(X,Y):
    a=len(X)
    b=len(Y)
    if a==0:
        return 0
    else:
        if X[-b:]==Y and X[:b]==Y:
            return len(X)
        if X[-b:]==Y:
            return strDist(X[1:],Y)
        if X[:b]==Y:
            return strDist(X[:-1],Y)
        else:
            return strDist(X[1:-1],Y)


















