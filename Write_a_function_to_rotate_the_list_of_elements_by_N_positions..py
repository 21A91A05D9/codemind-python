n=int(input())
s=list(map(int,input().split()))
r=int(input())
while r:
    t=s[n-1]
    s.insert(0,t)
    r-=1
for i in range(n):
    print(s[i],end=" ")