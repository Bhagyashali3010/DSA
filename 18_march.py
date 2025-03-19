# nums = [3,4,1,2]
# i=0
# while i<len(nums):
#     a=nums[i]
#     nums.remove(nums[i])
#     if a in nums :
#         b=nums.index(a)
#         nums.pop(b)
#         i=i
#     else:
#         print("no")
#         break

#     print("yes")


# n=7
# seen=set()
# while n!=1:
#     if n not in seen:
#         seen.add(n)
#         n=sum([int(x)**2 for x in str(n)])
#     else:
#         print("no")
#         break
# print(n==1)



nums= [2,2,3,9,9,4,4,4,1,1,1]
k = 2
dicti={}
s=set(nums)
print(s)
for i in s:
    c=nums.count(i)
    dicti[i]=c
final=[key for key,_ in (sorted(dicti.items(),key = lambda item: item[1], reverse = True)[:k])]
print(final)