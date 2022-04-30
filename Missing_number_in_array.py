n=int(input())
s=0
for i in range(n):
    a=int(input())
    ar=list(map(int,input().split()))
    s=0
    g=a*(a+1)//2
    for i in ar:
        s=s+i
    print(abs(s-g))