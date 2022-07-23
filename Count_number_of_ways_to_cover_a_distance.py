n=int(input())
a=1;b=1;c=2
if n==1:
    print("1")
elif n<=2:
    print(n)
else:
    for i in range(3,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
    print(d)
        