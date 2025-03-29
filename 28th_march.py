#1

# s = "hello"
# sum=0
# diff=0
# for i in range (len(s)-1):
#     diff=abs(ord(s[i])-ord(s[i+1]))
#     sum+=diff

# print (sum)


#2

# boxes = "001011"
# arr=[]
# for i in range (len(boxes)):
#     moves=0
#     for j in range(len(boxes)):
#         if i==j or boxes[j]=='0':
#             pass
#         else:
#             moves+=abs(i-j)
#     arr.append(moves)
#     print(arr)


#3
# n = "82734"
# maxi=0
# for i in range(len(n)):
#     a=int(n[i])
#     maxi=max(a, maxi)
# print(maxi)


#4
maxi=0
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
for i in range(len(sentences)):
    count=0
    for j in range(len(sentences[i])):
        if (sentences[i][j])==' ':
            count+=1

    maxi=max(maxi,count)
    print(maxi+1)