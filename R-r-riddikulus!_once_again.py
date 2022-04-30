a,b=map(int,input().split())
ar=list(map(int,input().split()))
for i in range(0,a):
    if i>=b:
        print(ar[i],end=" ")
for i in range(0,a):
    if i<b:
        print(ar[i],end=" ")