n=6
s='111011'
cash=7
b=3            
a=2
s=list(s)

if b<a:
    if '0' in s:
        print('d')
        z=s.index('0')
        s[0],s[z]=s[z],s[0]
        cash-=b
        for i in range(1,len(s)):
            if s[i]=='1':
                if cash>=a:
                    s[i]='0'
                    cash-=a
    else:
        for i in range(len(s)):
            if s[i]=='1':
                if cash>=a:
                    s[i]='0'
                    cash-=a
else:
    for i in range(len(s)):
        if s[i]=='1':
            if cash>=a:
                s[i]='0'
                cash-=a
s=''.join(s)
num=int(s,2)
print(num, cash)


