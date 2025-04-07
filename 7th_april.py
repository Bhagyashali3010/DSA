#1
# from collections import defaultdict 

# s="abccdcabacdadbccaa"
# dicti=defaultdict(int)
# for i in range (len(s)):
#     dicti[s[i]]+=1
# print(dicti)
# mini=min(dicti.values())
# print("mini",mini)
# if mini==1:
#     print(1)
# else:
#     for value in dicti.values():
#         if value%mini ==0:
#             print(mini)
#         else:
#             print(1)
#             break
    


#2
# n=4
# l=[-1,1,1,1]
# if all(l[i]>l[i+1] for i in range(len(l)-1)):
#     print(0)
# maxi=0
# L=l[:]
# for i in range(1, len(L)):
#     if l[i]>=L[i-1]:
#         diff=L[i]-(L[i-1]-1)
#         L[i]==diff
#         maxi=max(maxi, diff.bit_length())
#     print(maxi)

#partially completed


#3
class Solution(object):
    def steps(self, cost, n):
        prev1=cost[1]
        prev2=cost[0]

        for i in range(2, n):
            curr=cost[i]+min(prev1, prev2)
            prev2=prev1
            prev1=curr
        return min(prev1, prev2)

    def minCostClimbingStairs(self, cost):
        n=len(cost)
        return self.steps(cost, n)
        