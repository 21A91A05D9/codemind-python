import math
s=list(map(int,input().split(",")))
flag=0;l=[]
for i in s:
    v=0
    t=i
    for j in range(1,int(math.sqrt(t))+1):
        if t%j==0:
            if j*j==t:
                v+=j
            else:
                v+=j
                v+=(t//j)
    if v in s:
        l.append(i)
if len(l)!=0:
    print(*sorted(l))
else:
    print("-1")