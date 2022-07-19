a,b,c=map(int,input().split())
s=list(map(int,input().split()))
while b:
    t=s[a-1]
    s.insert(0,t)
    b-=1
while c:
    a=int(input())
    print(s[a])
    c-=1