a,b=map(int,input().split())
for i in range(0,a):
    s=0
    d=list(map(int,input().split()))
    for j in d:
           s=s+j
    print(s,end=" ")
