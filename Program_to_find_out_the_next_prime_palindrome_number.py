import math
n=int(input())
i=n+1
v=0
while 1:
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            i+=1
            break
    else:
        h=str(i)
        if h==h[::-1]:
            v=1
            print(i)
            break
        else:
            i+=1
    if v==1:
        break
    