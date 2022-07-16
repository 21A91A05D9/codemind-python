a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0;v=0
    t=i
    if t<10:
        print(t,end=" ")
    else:
        while t:
            r=t%10
            if r==0:
                c=1
                break
            c+=1
            if i%r==0:
                v+=1
            t=t//10
        if c==v:
            print(i,end=" ")