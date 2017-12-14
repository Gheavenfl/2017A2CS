
array=[123,321,132,231,312,456,111]
len=len(array)
for s in range(len-1):
    
    for i in range(len-1):
        if array[i]>array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
  
        i=i-1
print array
                        
