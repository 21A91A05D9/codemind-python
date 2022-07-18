n=int(input())
s=list(map(int,input().split()))
v=sorted(s,reverse=True)
for i in range(0,n-1,+2):
    v[i],v[i+1]=v[i+1],v[i]
print(*v)