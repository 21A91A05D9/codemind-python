n=int(input())
a=map(int,input().split())
a=list(a)
for i in range(n):
    if a[i]==0:
        t=a[i]
        for j in range(i,n-1):
            a[j]=a[j+1]
        a[n-1]=t
i=0
while a[i]==0:
    for l in range(n):
           if a[l]==0:
               t=a[l];
               for j in range(l,n-1):
                   a[j]=a[j+1]
                   a[n-1]=t
for i in range(n):
    print(a[i],end=" ")
