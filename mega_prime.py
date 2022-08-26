import math
n=int(input())
v=0
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        v=1
        break
else:
    c=0
    h=0
    t=n
    while t:
        r=t%10
        if r==1 or r==0:
            c=1
            h=0
            break
        for i in range(2,int(math.sqrt(r))+1):
            if r%i==0:
                break
        else:
            c+=1
        h+=1
        t=t//10
    if c==h:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
if v==1:
    print("Not Mega Prime")