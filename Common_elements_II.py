a,b=map(int,input().split())
s=list(map(int,input().split()))
v=list(map(int,input().split()))
l=[]
for i in s:
    if i not in v and i not in l:
        l.append(i)
for i in v:
    if i not in s and i not in l:
        l.append(i)
print(*l)