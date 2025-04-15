#1
# def fun(str1, str2):
#     if str2+str1 != str1+str2:
#         return ("")
#     if len(str1) == len(str2):
#         return str1
#     if len(str1) > len(str2):
#         return fun(str1[len(str2):], str2)
#     return fun(str1, str2[len(str1):])

# str1 = "ABCABC"
# str2 = "ABC"
# print(fun(str1, str2))   



#2
# s = "the sky is blue"
# l=list(s.split())
# rev=''
# for i in range(len(l)-1,-1,-1):
#     rev+=l[i]
#     if i>0:
#         rev+=' '
#     print(rev)

#3
# nums = [1,2,3,4]
# n=len(nums)
# prod=[1]*n
# prefix=1
# suffix=1
# for i in range(n):
#     prod[i]=prefix
#     prefix*=nums[i]
#     print(prod)
# for i in range(n-1,-1,-1):
#     prod[i]*=suffix
#     suffix*=nums[i]
#     print(prod)



#4
# nums = [1,2,3,4]
# k=5
# c=0
# nums.sort()
# i=0
# j=len(nums)-1 
# while i<j:
#     if nums[i]+nums[j]==k:
#         c+=1
#         nums.pop(j)
#         nums.pop(i)
#         i=0
#         j=len(nums)-1 
#     elif nums[i]+nums[j]<k:
#         i+=1
#     elif nums[i]+nums[j]>k:
#         j-=1
#     print(nums)
# print(c)


#5
# nums = [1,12,-5,-6,50,3]
# k = 4
# l=0
# r=0
# maxi=0
# c=0
# avg=0
# while r<len(nums):   
#     avg+=nums[r]
#     c+=1
#     r+=1
#     if c==k:
#         maxi=max(maxi, avg/k)
#         avg-=nums[l]
#         l+=1
#         c-=1
# print(maxi)



#6
# arr = [1,2]
# dicti={}
# for i in range(len(arr)):
#     if arr[i] in dicti:
#         dicti[arr[i]]+=1
#     else:
#         dicti[arr[i]]=1
#     print(dicti) 
# v=list(dicti.values())
# s=set(v)
# if len(s)==len(v):
#     print(True)
# else:
#     print(False)
# print(v, s)

#7
word1="abbzzca"
word2="babzzcz"
if len(word1)!= len(word2):
    print (False)
if len(set(word1))!= len(set(word2)):
    print (False)
dicti1={}
dicti2={}
for i in range(len(word1)):
    if word1[i] in word2:
        if word1[i] in dicti1:
            dicti1[word1[i]]+=1
            dicti2[word2[i]]+=1
        else:
            dicti1[word1[i]]=1
            dicti2[word2[i]]=1
        print(dicti1, dicti2)
    else:
        print (False)
l1= (list(dicti1.values()))
l2= (list(dicti2.values()))
print(l1, l2)
print (sorted(l1)==sorted(l2))
    #     print(l1, l2)
    #     print (True)
    # else:
    #     print (False)