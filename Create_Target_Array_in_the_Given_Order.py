a=int(input())
s=list(map(int,input().split()))
b=int(input())
v=list(map(int,input().split()))
m=[]
for i in range(b):
    m.insert(v[i],s[i])
print(*m)
        
        
    