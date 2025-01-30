pwr=[101,100,524,98,420]
bon=[110,110,3,100,10]
n=5
exp=100
count=0
d={}
for i ,(p,b) in enumerate(zip(pwr,bon)):
    d[p]=b
    # print(d)
pwr.sort()
for i in range (n):
    if pwr[i]<=exp:
        count+=1
        g=d.get(pwr[i])
        exp+=g
        print(count)
