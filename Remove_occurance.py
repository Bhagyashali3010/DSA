s = "aabababa"
part = "aba"
for i in range (len(s)):
    if part in s:
        s=s.replace(part,"",1)
        print(i,s,len(s))
        i=i
    else:
        i+=1



