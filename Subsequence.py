A=[2,8,12,2,8,17,17]
n=7
S=[]
B=[]
for i in range (n-1):
    x=(( A[i] & A[i+1] ) * 2 )
    y=( A[i] | A[i+1] )
    print (x,y,i,i+1,x-y)
    if ( x < y):
        print("ok")
        if A[i]<A[i+1]:
            if len(S)==0:
                B.append(A[i])
                B.append(A[i+1])
                new=i+1
            
            elif i==new:
                    B.append(A[i+1])
                    new=i+1
            else:
                 B=[]
                 B.append(A[i])
                 B.append(A[i+1])
                 new=i+1
            S.append(B)
            print(A[i],A[i+1],S,B)
