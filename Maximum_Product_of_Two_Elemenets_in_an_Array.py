a=list(map(int,input().split()))
n=len(a)
k=0
v=0;m=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if a[i]*a[j]>k:
                k=a[i]*a[j]
                v=i
                m=j
print((a[v]-1)*(a[m]-1))