allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
count=0
first=list(allowed)
print(first)
for i in range(len(words)):
    check=list(words[i])
    for j in check:
        if j in first:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        count+=1
print(count)    
