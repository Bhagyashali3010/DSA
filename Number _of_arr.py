n=3
k=3
def counter(n,k):
    s=0
    if k==1:
        return n
    else:
        for i in range (1,n+1):
           for j in range (1,n+1): 
               if j%i==0:
                    s+=1
    return s  
    
def count(n,k):
    if k==1:
        return n
    elif k==2:
        return (counter(n,k))
    else:
        mid=k//2
        x=count(n,k-mid)
        y=counter(n,mid)
        return x+y-1    
print(count(n,k))