a,b=map(int,input().split())
v=[1,2,3,4,5,6,7,8,9,10,1]
p=0
for i in range(len(v)-1):
    if v[i]==a and v[i+1]==b:
        print("Yes")
        p=1
        break
    elif v[i]==b and v[i+1]==a:
        print("Yes")
        p=1
        break
if p==0:
    print("No")