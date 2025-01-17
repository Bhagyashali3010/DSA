from itertools import combinations

def fun(arr, n):
    max_xor=max(arr)
    sub=[]
    for i in range (1,n//2):
        comb=combinations(arr,i+1)        
        for i in comb:
            sub.append(list(i))
    for a in comb:          
        z=0
        for b in a:
            z=z^b
        if z>max_xor:
            max_xor=z
    return max_xor

arr=[1,2,4,8,10,24]
n=len(arr)
if n<3:
    print (max(arr))
else:
    print(fun(arr,n))