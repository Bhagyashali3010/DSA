# n=2
# l=[3,2]     #[-1,1,1,1]
# while all(l[i]>l[i+1] for i in range (len(l)-1)):
#     for j in range()
#     print(l)
#     break


#2
n=6
arr=[3,3,4,4,5,5]
count=0
mid=n//2
if mid%2==0:
    i=mid-1
    j=mid+1
    for k in range(mid, 0,-1):
        if arr[i]==arr[j]==arr[mid]-1:
            pass
        elif arr[i]==arr[mid]-1:
            arr[j]!=arr[mid]-1
            arr[j]=arr[i]
            count+=1
        elif arr[j]==arr[mid]-1:
            arr[i]!=arr[mid]-1
            arr[i]=arr[j]
            count+=1
        else:
            arr[i]=arr[j]=arr[mid]-1
            count+=2
        mid=i
        i-=1
        j+=1
        print(count, arr)

if mid%2!=0:
    j=mid
    i=mid-1
    for k in range(mid,0,-1):
        if arr[i]==arr[j]:
            pass
        elif arr[i]==arr[i+1]-1:
            arr[j]=arr[i]
            count+=1
        elif arr[j]==arr[j-1]-1:
            arr[i]=arr[j]
            count+=1
        else:
            arr[i]=arr[j]=arr[i+1]-1
            count+=2
        i-=1
        j+=1
        print(count, arr)



