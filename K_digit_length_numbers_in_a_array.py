a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in s:
    if i<0:
        i=str(i)
        if(len(i)-1==b):
            c+=1
    else:
        i=str(i)
        if(len(i)==b):
            c+=1
print(c)