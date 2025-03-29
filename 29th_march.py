#1

# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"
# dicti={}
# alpha="abcdefghijklmnopqrstuvwxyz"
# key="".join(key.split())
# i=0
# j=0
# while j<(len(key)):
#     if key[j] not in dicti.keys():
#         dicti[key[j]]=alpha[i]
#         i+=1
#         j+=1
#     else:
#         j+=1

# print(dicti)
# ans=''
# for i in range(len(message)):
#     if message[i]==" ":
#         ans+=' '
#     else:
#         ans+=dicti[message[i]]
# print(ans)


#2
# n=3
# arr=[]
# def strings(s, rem):
#     if rem==0:
#         arr.append(s)
#         return
#     if s[-1]!='0':
#         strings(s+'0',rem-1)
#     strings(s+'1', rem-1)
# strings("1", n-1)
# strings("0", n-1)
# print(arr)


#3
# piles=[4,4,17,7,16,16,16,15,2,3,1,17,6,12,9]
# piles.sort(reverse=True)
# i=0
# coins=0
# while len(piles)!=0:
#     piles.remove(piles[i])
#     coins+=piles[i]
#     piles.remove(piles[i])
#     piles.pop()
# print (coins)


#4
deck = [17,13,11,2,3,5,7]
deck.sort()
ans=[0]*len(deck)
i=0
k=0
q=[x for x in range(len(deck))]
while (len(q))!=0:
    if len(q)<=2:
        ans[k]=deck[i]
        ans[q[1]]=deck[i+1]
        q.pop()
        q.pop()
        
        
    else:
        ans[k]=deck[i]
        q.pop(0)
        q.append(q[0])
        q.pop(0)
        k=q[0]

        
    i+=1
    print("ans",ans)


