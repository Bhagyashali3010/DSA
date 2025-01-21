n=10
m=5
k=2
arr=[3,2,6,7,9]
days=0
i=1
d=0
while i<n+1:
    if i not in arr:
        if i==(days+1):
            days+=1
        else:
            d+=1
        i+=1       
    else:
        if k>0:
            days+=1
            k-=1
        else:
            days=days
        i+=1
    print(i-1, days, d)
    maxi=max(d,days)    
print(maxi)






