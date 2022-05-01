s=str(input())
c=0;d=0
for i in s:
    if i=='z':
        c+=1
    if i=='o':
        d+=1
if 2*c==d:
    print("Yes")
else:
    print("No")