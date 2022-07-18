n=int(input())
s=list(map(int,input().split()))
a=int(input())
g=0
v=s[::-1]
if a in s:
    print(s.index(a),end=" ")
    g=1
if a in v:
    print(n-(v.index(a))-1)
    g=1
if g==0:
    print("-1 -1")