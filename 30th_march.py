#1
# mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# one=[]
# for i in range (len(mat)):
#     one+=mat[i]
# one.sort()
# n=len(mat[0])
#incomplete



#2
# nums = [5,6,2,7,4]
# nums.sort()
# pair1=(nums[-1], nums[-2])
# pair2=(nums[0], nums[1])
# sum=(pair1[0]*pair1[1])-(pair2[0]*pair2[1])
# print(sum)


#3
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2]]
res=[]
i , j= 0,0
while i<len(nums1) and j<len(nums2):
    id1, val1 = nums1[i]
    id2, val2 = nums2[j]

    if id1<id2:
        res.append([id1, val1])
        i+=1
    elif id2<id1:
        res.append([id2, val2])
        j+=1        
    else:
        res.append([id1, val1+val2])
        j+=1
        i+=1
while i<len(nums1):
    res.append(nums1[i])
    i+=1
while j<len(nums2):
    res.append(nums2[j])
    j+=1
print (res)
