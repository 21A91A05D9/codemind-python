a=input()
a=a.lower()
a=a.split()
x={'a','e','i','o','u'}
l=[];mi=0;v=0
for i in a:
    c=0
    v+=1
    for j in i:
        if j in x:
            c+=1
    if v==1:
        mi=c
    if c<=mi:
        mi=c
        l.append(mi)
print(l.count(mi))
    
        