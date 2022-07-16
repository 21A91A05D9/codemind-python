n=int(input())
m=str(n)
v=1;s=0
for i in m:
    s=s+(pow(int(i),v))
    v+=1
if s==n:
    print("True")
else:
    print("False")
