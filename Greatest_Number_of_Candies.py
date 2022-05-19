n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=max(a)
for i in range(0,n):
    if a[i]+k>=b:
        print("True",end=" ")
    else:
        print("False",end=" ")