a=str(input())
b=str(input())
a=a.lower()
m=0
for i in a:
    m+=1
b=b.lower()
v=0
for i in a:
    c=0
    for j in b:
        if i==j:
            c+=1
    if c>=1:
        v+=1
if v==m:
    print("True")
else:
    print("False")