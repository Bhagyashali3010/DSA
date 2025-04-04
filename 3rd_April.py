#1

# arr = ["d","b","c","b","c","a","c"]
# k = 2
# d=[]
# p=[]
# for i in arr:
#     if i not in d and i not in p:
#         d.append(i)
#     elif i in p:
#         pass
#     else:
#         p.append(i)
#         d.remove(i)
#     print(d, p)
# if len(d)>=k:
#     print(d[k-1])
# else:
#     print("")



#2
# word1 = "abc"
# word2 = "pqrs"
# s=''
# i=0
# j=0
# n=max(len(word1), len(word2))
# if n==len(word2):
#     while j<n:
#         if i<len(word1):
#             s+=word1[i]
#             i+=1
#         s+=word2[j]
#         j+=1
#     print(s)
# else:
#     while i<n:
#         s+=word1[i]
#         if j<len(word2):
#             s+=word2[j]
#             j+=1
#         i+=1
# print(s)



#3
# rings = "B0B6G0R6R0R6G9"
# # count=0
# for i in range(10):
#     i=str(i)
#     if 'R'+i in rings and 'B'+i in rings and 'G'+i in rings:
#         count+=1
# print(count)
            

#4
# co='a1'
# dicti={'a':'1', 'b':'2', 'c':'3', 'd':'4','e':'5', 'f':'6', 'g':'7', 'h':'8'}
# co=co.replace(co[0], dicti[co[0]])
# sum=int(co[0])+int(co[1])
# if sum%2==0:
#     print(False)
# else:
#     print(True)



#5
word = "zjpc"
dist=len(word)
p="a"
for i in word:
    l=(ord(i)-ord(p))%26
    dist+=min(l, 26-l)
    p=i
    print(dist)


