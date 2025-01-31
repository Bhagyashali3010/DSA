words = ['a','b']
r1="qwertyuiop"
r2="asdfghjkl"
r3="zxcvbnm"
res=[]
flag=0
for word in words:
    if len(word)==1:
        res.append(word)
    else:
        dum=word
        word=word.lower()    
        j=0
        row=r1
        while j<(len(word)):
            if j==0:
                if word[j] in r1:
                    row=r1
                if word[j] in r2:
                    row=r2
                if word[j] in r3:
                    row=r3
                word=word[j].upper()+word[j+1:]
                print(word[j],word)
                j+=1

            else:
                if word[j] in row:
                    flag=1
                    j+=1
                else:
                    flag=0
                    j=len(word)
            print(flag,j)    
        if flag==1:
            # word[0].upper()+word[]
            res.append(dum)
    print(res)