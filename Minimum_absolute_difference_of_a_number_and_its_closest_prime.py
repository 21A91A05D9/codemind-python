import math
n=int(input())
v=0
for i in range(n,0,-1):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        c=abs(n-i)
        v=1
        break
    if v==1:
        break
i=n+1
v=0
while 1:
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            i+=1
            break
    else:
        d=abs(n-i)
        v=1
        break
    if v==1:
        break
print(min(c,d))
        