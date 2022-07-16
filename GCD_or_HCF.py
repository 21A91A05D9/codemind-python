a,b=map(int,input().split())
c=min(a,b)
lcm=1
for i in range(2,c+1):
    if a%i==0 and b%i==0:
        lcm=i
print(lcm)