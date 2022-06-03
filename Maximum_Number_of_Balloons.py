a=input()
l=[]
z=0;x=0;c=0;v=0;b=0
for i in a:
    if i=='b':
        z+=1
    elif i=='a':
        x+=1
    elif i=='l':
        c+=1
    elif i=='o':
        v+=1
    elif i=='n':
        b+=1
c=c//2
v=v//2
l.append(z)
l.append(x)
l.append(c)
l.append(v)
l.append(b)
p=min(l)
print(p)
