a=input()
a=a.lower()
a=a.split()
b=a[0];v="";m=0
for i in b:
    c=0
    for j in range(1,len(a)):
        m=a[j].count(i)
        if m>0:
            c+=1
    if c==(len(a)-1):
        v+=i
if v!="":
    print(v)
else:
    print("-1")