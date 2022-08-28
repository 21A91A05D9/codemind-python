n=input()
c=0
for i in n:
    if i.isupper():
        c+=1
if n[0].islower():
    c+=1
print(c)