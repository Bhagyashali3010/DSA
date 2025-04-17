from collections import defaultdict

def count_valid_quadruples(x):
    n = len(x)
    count = 0

    # map to keep count of (char_a, char_b) pairs before position c
    pair_count = defaultdict(int)
    # 
#wverealjagsegi
    for c in range(1, n):
        for d in range(c + 1, n):
            # x[a] == x[c] and x[b] == x[d]
            char_c = x[c]
            char_d = x[d]
            count += pair_count[(char_c, char_d)]

        # Update pair_count with all (a, b) pairs where b == c
        for a in range(c):
            pair_count[(x[a], x[c])] += 1

    return count


#3
# n=int(input("n:"))
# arr=[None]*n
# for i in range(n):
#     arr[i]=int(input())
# k=int(input("k:"))
# a=arr[0]
# mini=0
# for i in range(1,k+1):
#     if arr[i]<arr[mini]:
#         mini= i
#     if arr[i]==arr[mini]:
#         mini=i
# arr[0], arr[mini] = arr[mini], arr[0]
# print(arr, a, mini)


    
#4
n=int(input("n:"))
arr=[None]*n
for i in range(n):
    arr[i]=int(input())
c=0
dicti={}
for i in range(n):
    dicti[arr[i]]=dicti.get(arr[i],0)+1
    d=dict(sorted(dicti.items(), key=lambda item:item[1]))
for i in (d.values()):
    if c==0:
        c+=i
        a=2*i
    else:
        if i>=a:
            c+=a
print(c)