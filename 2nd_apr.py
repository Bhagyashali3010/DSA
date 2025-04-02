#1

# nums = [1,13,10,12,31]
# l=len(nums)
# s=set()
# for i in range (l):
#     if nums[i] not in s:
#         s.add(nums[i])
#     st=str(nums[i])
#     n="".join(reversed(st))
#     n=int(n)
#     s.add(n)
#     print(len(s))



#2
# prices = [7,1,5,3,6,4]
# i=0
# j=1
# maxi=0
# while j<len(prices):
#     diff= prices[j]-prices[i]
#     if prices[i]<prices[j]:
#         maxi=max(maxi, diff)
#     else:
#         i=j
#     j+=1
#     print(i,j,maxi)



#3
# nums = [0,2,3,4,6,8,9]
# i=0
# j=1
# arr=[]
# if len(nums)==1:
#     (arr.append(str(nums[i])))
#     return arr
# else:
#     while j<len(nums):
#         if nums[j]-1==nums[j-1]:
#             if j==len(nums)-1:
#                 arr.append(str(nums[i])+"->"+str(nums[j]))
#             j+=1
#         elif i+1==j and nums[j]-1!=nums[j-1]:
#             arr.append(str(nums[i]))
#             i=j
#             j+=1
#             if j==len(nums):
#                 arr.append(str(nums[i]))
#         else:
#             arr.append(str(nums[i])+"->"+str(nums[j-1]))
#             i=j
#             j+=1
#             if j==len(nums):
#                 arr.append(str(nums[i]))
#     print(arr)



#4
# nums = [0,1]
# for i in range (len(nums)+1):
#     print(i)
#     if i not in nums:
#         print(i)


#5
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
for i in range(len(board)):
    for j in range(len(board[i])):
        count1=0
        count0=0
        curr=board[i][j]
        if board[i][j+1]==1:
            count1+=1
        else:
            count0+=1
        
                

