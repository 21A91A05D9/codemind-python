n=int(input())
a=map(int,input().split())
a=list(a)
for i in range(n-1,n//2-1,-1):
    print(a[i],end=" ")
for i in range(0,n//2,+1):
    print(a[i],end=" ")

    