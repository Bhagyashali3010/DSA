#1
# n=int(input("n:"))
# e=int(input("e:"))
# power=[]
# bonus=[]
# combine=[]
# count=0
# for i in range(n):
#     power.append(int(input("p:")))
# for i in range(n):
#     bonus.append(int(input("b:")))
# for j in range(n):
#     combine+=[[power[j], bonus[j]]]
# combine.sort()
# for k in combine:
#     if k[0]>e:
#         break
#     e+=k[1]
#     count+=1
# print(count)




#2
# s = "bhh"
# i=0
# j=len(s)-1
# l=list(s)
# while i<(len(l)//2) and j>(len(l)//2):
#     if l[i]==l[j]:
#         i+=1
#         j-=1
#     else:
#         if ord(s[i])<ord(s[j]):
#             l[j]=l[i]
#         else:
#             l[i]=l[j]
#         i+=1
#         j-=1
#     print("".join(l))


#3
# s = "il**autonrd**cl**nh*up*afpizp****d*a****lst"
# li=list(s)
# i=0
# l=len(li)
# while i<len(li):
#     if li[i]=='*':
#         li.pop(i)
#         li.pop(i-1)
#         i-=1

#     else:
#         i+=1
# s=''.join(li)
# print(s)




#4
# e=6
# ex=3
# arr=[1,2]
# r=0
# count=0
# arr.sort(reverse=True)
# for i in range(len(arr)):
#     if e>0 :
#         if e==arr[i]:
#             e-=arr[i]
#             count+=1
#         elif arr[i]<e:
#         # r+=2*arr[i]
#             e-=2*arr[i]
#             count+=2
#         else:
#             i+=1
# if e==0:
#     print(count)
# else:
#     print(-1)




#5
n=5
m=1
h=4
arr=[1,2,3,1,3]
hero_h=m*h
villan_h=0
for i in range(n-1,-1,-1):
    if arr[i]<=h:
        print("arr",arr[i], "h",h)
        villan_h+=arr[i]
        hero_h-=arr[i]
        print(villan_h, hero_h)
        if hero_h==0:
            print("else:",i)
            break

    else:
        print("else:",i+1)
        break
    print(i)
        
    


