colors = "AAAAABBBBBBAAAAA"
l=len(colors)
alice=0
bob=0
i=0
while i<l:
    if i%2==0:
        if "AAA" in colors:
            a="AAA"
            colors=colors.replace(a,"AA",1)
            print(colors)
            alice+=1
            i+=1
        else:
            break
        print(alice,bob)
    else:
        if "BBB" in colors:
            a="BBB"
            colors=colors.replace(a,"BB",1)
            print(colors)
            bob+=1
            i+=1
        else:
            break 
        print(alice,bob)
if alice>bob:
    print(True)
else:
    print(False)

    