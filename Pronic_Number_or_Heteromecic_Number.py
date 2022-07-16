n=int(input())
v=0
for i in range(1,n+1):
    if i*i+1==n:
        v=1
        print("NO")
        break
if v==0:
    print("YES")
    