strs = ["ddddddddddg","dgggggggggg"]
i=0
count=[]
while i<(len(strs)):
    arr=[]
    a=strs[i]
    arr.append(a)
    b=i+1
    while b<len(strs):
        if len(a)!=len(strs[b]):
            b+=1
        else:
            flag=1
            for c1 in strs[b]:
                if c1 in a and a.count(c1)==strs[b].count(c1):
                    flag=1
                else:
                    flag=0
                    break
            print(a, strs[b], flag)
            if flag==1:
                arr.append(strs[b])
                strs.remove(strs[b])
                b=b
            else:
                b+=1
    strs.remove(a)
    count.append(arr)
    i=i
print(count)


        