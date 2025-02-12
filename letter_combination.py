digits = "23"
from itertools import combinations
temp=[]
s= {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",
     '8':"tuv", '9':"wxyz"}
if len(digits)==0:
    print(temp)
if len(digits)==1:
    val=s.get(digits)
    for i in val:
        temp.append(i)
    print(temp)
else:
    for i in range(len(digits)-1):
        num=s.get(digits[i])
        print(num)
        num2=s.get(digits[i+1])
        for j in num:
            print(j)
            for k in num2:
                ele=j+k
                temp.append(ele)
        print(temp)
            # comb = [(j) + c for c in combinations(s.get(digits[i+1]), 2)]
        # print(comb)