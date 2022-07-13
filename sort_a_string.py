k=input()
s=k.split()
c=""
for i in k:
    if i.isalnum():
        c+=i
c=sorted(c)
k=list(k)
v=0
for i in range(len(k)):
    if k[i].isalnum():
        k[i]=c[v]
        v+=1
print("".join(k))
        
    