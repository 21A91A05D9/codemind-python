a=input()
a=a.lower()
a=a.split()
x={'a','e','i','o','u'}
for i in a:
    c=0
    for j in i:
        if j in x:
            c+=1
    print(c,end=" ")
        