n=int(input())
s=list(map(int,input().split()))
v=[]
for i in range(1,n):
    v.append(max(s[i:]))
v.append(-1)
print(*v)