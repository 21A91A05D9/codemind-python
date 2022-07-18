a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in range(a):
    k=0
    for j in range(i,a):
        k+=s[j]
        if k==b:
            c+=1
            break
        elif k<b:
            continue
        else:
            break
print(c)
        
        
    

