a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
a=''.join(a)
b=''.join(b)
s=""
for i in a:
    if i not in b and i not in s:
        s+=i
for i in b:
    if i not in a and i not in s:
        s+=i
print(len(s))