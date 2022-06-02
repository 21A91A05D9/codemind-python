a=input()
c=0;v=0;n=0
for i in a:
    if i=='L':
        c+=1
    if i=='R':
        v+=1
    if c==v:
        n+=1
print(n)