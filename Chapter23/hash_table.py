# Harvey S3C3 Op1
# Hash Table Version 1

hash=[None for i in range(10)]

def Hash(key):
    address=key%10
    return address

def Insert(key):
    Index=Hash(key)
    while hash[Index]!=None:
        Index+=1
        if Index>9:
            Index=0
    hash[Index]=key

def Find(search):
    Index=Hash(search)
    loop=0
    while hash[Index]!=search and hash[Index]!=None:
        Index+=1
        if Index>9:
            Index=0
            loop+=1
        if loop>1:
            break
    if hash[Index]!=None:
        return Index

Insert(12)
Insert(23)
Insert(222)
Insert(564)
print hash

