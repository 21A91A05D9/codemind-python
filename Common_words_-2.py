a=input()
b=input()
a=a.upper()
b=b.upper()
a=a.split()
b=b.split()
c=0
for i in a:
    for j in b:
        if i==j:
            z=a.count(i)
            x=b.count(j)
            if z==1 and x==1:
                c+=1
                break
print(c)