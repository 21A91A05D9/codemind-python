def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
v=0
for i in range(1,n+1):
    a=isprime(i)
    if a==1:
        for j in range(1,n+1):
            b=isprime(j)
            if b==1 and i*j==n:
                print(i,j)
                v=1
                break
        if v==1:
            break
if v==0:
    print("-1")
    