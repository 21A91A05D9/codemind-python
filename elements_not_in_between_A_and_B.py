n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
a=min(a,b)
b=max(a,b)
v=0
for i in s:
    if i<a or i>b:
        v=1
        print(i,end=" ")
if v==0:
    print("-1")
        