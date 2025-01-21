n=7
m=2
k=0
b=k
arr=[3,4]
days=0
maxi=0
if k==0:
    for i in range (1,n+1):
        if i not in arr:
            days+=1 
        else:
            days=0
        maxi=max(maxi,days)
else:
    
    for i in range (1,n+1):
        if i not in arr:
            days+=1   
        elif k>0 :
            days+=1
            k-=1        
        else:
            k=b
            days=0
            days+=1
            k-=1
        maxi=max(maxi,days)
        print(i,k,days,maxi)

print(maxi)
        









