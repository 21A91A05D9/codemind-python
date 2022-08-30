n=input()
a=['a','e','i','o','u']
v=''
for i in n:
    if i in a:
        a.remove(i)
a.sort()
if len(a)!=0:
    print(*a)
else:
    print("0")