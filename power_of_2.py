n=8
def trying(n):
    if n==0:
        return 1
    else:
        return (2*trying(n-1))

print(trying(4))

def another(n):
    if n==0:
        return False
    else:
        return (n==1 or (n%2==0 and another(n//2)))
    
print(another(34))