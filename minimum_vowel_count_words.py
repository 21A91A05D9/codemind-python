s=input().split()
mi=10000;b=0
for i in s:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    if c<mi:
        mi=c
for i in s:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    if c==mi:
        b+=1
print(b)
    
    