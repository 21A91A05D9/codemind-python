import math
a=int(input())
while a:
    n=int(input())
    v=0
    for i in range(n,0,-1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            c=i
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
            d=i
            v=1
            break
        if v==1:
            break
    if(abs(n-c)==abs(n-d)):
        print(c)
    elif(abs(n-c)>abs(n-d)):
        print(d)
    else:
        print(c)
    a-=1
        