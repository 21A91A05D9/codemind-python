a=input()
a=a.lower()
a=a.split()
a=''.join(a)
c=0;s=""
for i in a:
    c=a.count(i)
    if c==1:
        s+=i
s=list(s)
s.sort()
s=''.join(s)
print(s)