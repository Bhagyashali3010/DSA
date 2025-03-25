# n=int(input("length:"))
# arr= [int(input()) for _ in range(n)]
# # {7, 6, 8, 6, 1, 1}
arr=[12,2,2,5]
n=4
i=0
total=0
while len(arr)!=1:
    cost=0
    for i in range (2):
        a=min(arr)
        print("a=", a)
        # ind=arr.index(a)
        cost+=a
        arr.remove(a)
        print(cost)
    arr.append(cost)
    total+=cost
    print("total",total)
    i+=1


