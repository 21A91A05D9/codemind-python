a=input()
a=a.split()
s=[]
for i in a:
    s.append(i[::-1])
print(*s)