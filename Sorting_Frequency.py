n=int(input())
arr=list(map(int,input().split()))
v=set(arr)
v=list(v)
v=sorted(v)
s=[]
for i in v:
    s.append(arr.count(i))
p=sorted(s,reverse=True)
for i in range(len(p)):
    for j in range(len(s)):
        if s[j]==p[i]:
            t=j
            print(v[j],end=" ")
            v[j]=0
            s[j]=0
            break