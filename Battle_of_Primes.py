a=int(input())
b=int(input())
c=a+b
t=c+1
while 1:
    v=0
    for j in range(1,t+1):
        if t%j==0:
            v+=1
    if v==2:
        print(j-c)
        break
    t+=1
        
    