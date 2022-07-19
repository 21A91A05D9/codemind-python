n=int(input())
while n:
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    v=list(map(int,input().split()))
    s.extend(v)
    print(*sorted(s))
    n-=1