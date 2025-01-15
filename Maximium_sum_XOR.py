n=4
A=[7,4,0,3]
k=9
sum=0
maxi=0
for i in range (k):
    for j in range (n):
        sum=sum+(i^A[j])
    maxi=max(sum,maxi)
    sum=0

print(maxi)