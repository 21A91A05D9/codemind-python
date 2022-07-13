s=input().split()
for i in s:
    c=""
    for j in i:
        if j not in 'aeiou':
            c+=j
    c=sorted(c)
    i=list(i)
    k=0
    for j in range(len(i)):
        if i[j] not in 'aeiou':
            i[j]=c[k]
            k+=1
    i=''.join(i)
    print(i,end=" ")
    
            
