#S3C3 Harvey Op1
#recursion 2 code
def Groupsum(Y,X,Z):
    a=len(X)
    if Z==0:
        return True
    if Y==a:
        return False
    return Groupsum((Y+1),X,Z-X[Y]) or Groupsum((Y+1),X,Z)


def Groupsum6(Y,X,Z):
    a=len(X)
    if Z==0 and Y==a:
        return True
    if Y==a and Z!=0:
        return False
    if X[Y]==6:
        return Groupsum6((Y+1),X,Z-6)
    if Z==0 and Y!=a:
        return Groupsum6((Y+1),X,Z)
    else:
        return Groupsum6((Y+1),X,Z-X[Y]) or Groupsum6((Y+1),X,Z)


def Groupnoadj(Y,X,Z):
    a=len(X)
    if Z==0:
        return True
    if Y==a:
        return False
    if Y<a-1:
        return Groupnoadj((Y+2),X,Z-X[Y]) or Groupnoadj((Y+1),X,Z)
    else:
        return  Groupnoadj((Y+1),X,Z)


def Groupsum5(Y,X,Z):
    a=len(X)
    if Z==0 and Y==a:
        return True
    if Y==a and Z!=0:
        return False
    if Y<a:
        if X[Y]%5==0 and X[Y+1]!=1:
            return Groupsum5((Y+1),X,Z-X[Y])
        elif X[Y]%5==0 and X[Y+1]==1:
            return Groupsum5(Y+1,X,Z)
    if Z==0 and Y!=a:
        return Groupsum5((Y+1),X,Z)
    else:
        return Groupsum5((Y+1),X,Z-X[Y]) or Groupsum5((Y+1),X,Z)


def Groupsumclamp(Y,X,Z):
    a=len(X)
    if Z==0:
        return True
    if Y==a:
        return False
    if Y<a-1:
        if X[Y]==X[Y+1]:
            i=0
            while X[Y+i]==X[Y+i+1]:
                i+=1
            return Groupsumclamp(Y+i+2,X,Z) or Groupsumclamp(Y+i+2,X,Z-(i+1)*X[Y])
        else:
            return Groupsumclamp(Y+1,X,Z) or Groupsumclamp(Y+1,X,Z-X[Y])
    else:
        return Groupsumclamp(Y+1,X,Z) or Groupsumclamp(Y+1,X,Z-X[Y])


def Splitarray(X):
    a=len(X)
    if a==1 and X[0]==0:
        return True
    if a==1 and X[0]!=0:
        return False
    else:
        s=int(X[-1]+X[-2])
        d=int(X[-2]-X[-1])
        return Splitarray(X[:-2]+[s]) or Splitarray(X[:-2]+[d])


def Splitodd10(X):
    a=len(X)
    if a==1:
        if X[0]==10 or X[0]%2==1:
            return True
        else:
            return False
    if a==2 and X[-1]%10==0 and X[-2]%2==1:
        return True
    if a==2 and X[-2]%10==0 and X[-1]%2==1:
        return True
    if a==2 and X[-1]%10==0 and X[-2]&2!=1:
        return False
    if a==2 and X[-2]%10==0 and X[-1]&2!=1:
        return False
    else:
        return Splitodd10(X[:-2]+[X[-1]+X[-2]]) or Splitodd10([X[0]+X[1]]+X[2:]) or Splitodd10([X[0]+X[-1]]+X[1:-1]) or Splitodd10(X[1:-1]+[X[0]+X[-1]])


def  split53(X):
    return groupsum1(X,0,0)

def groupsum1(X,a,b):
    if len(X)==0:
        if a==b:
            return True
        else:
            return False
    else:
        if X[0]%5==0:
            return groupsum1(X[1:],a+X[0],b)
        if X[0]%3==0 and X[0]%5!=0:
            return groupsum1(X[1:],a,b+X[0])
        else:
            return groupsum1(X[1:],a+X[0],b) or groupsum1(X[1:],a,b+X[0])
