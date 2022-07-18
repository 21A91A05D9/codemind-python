n=int(input())
while n:
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    while b:
        t=s[a-1]
        s.insert(0,t)
        b-=1
        s.pop()
    print(*s)
    n-=1