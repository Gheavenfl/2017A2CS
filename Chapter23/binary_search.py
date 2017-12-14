list=[1,7,9,23,45,66,67,68,85,89,90,92,97,99,100]

def search(list, search):
    length=len(list)
    low=0
    high=length-1
    while  low<=high and low>-1:
        mid=(high+low)//2
        if list[mid]<search:
            low=mid+1
        elif list[mid]>search:
            high=mid-1
        elif list[mid]==search:
            return mid
    return -1

value=int(input('the value intended'))
a=search(list, value)
print (a)
