cases=int(input())
start=-1
end=-1
size=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
    # print(size)
    # print(arr1)
    # print(arr2)
for j in range (len(arr1)):
    if arr1[j]!=arr2[j]:
            if start==-1:
                    start=j
            end=j

if start==-1:
    print(0)
else:
    print(end-start+1)

