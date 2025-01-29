# arr = [1, 3, 5]
n=6
arr=[]
for i in range(0,n):
    arr.append((2*i)+1)
print(arr)

if n%2!=0:
    x=arr[(n//2)+1]
    sum=0
    for i in range (n//2,0,-1):
        y=arr[i]
        sum+=(x-y)
else:
    x=(arr[(n//2)-1])+1
    sum=0
    for i in range ((n//2)-1,-1,-1):
        y=arr[i]
        sum+=abs(x-y)
    


print(sum)    
