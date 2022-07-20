def gcf(a,b):
    if b==0:
        return a
    return gcf(b,a%b)
n=int(input())
s=list(map(int,input().split()))
v=gcf(s[0],s[1])
for i in range(2,n):
    v=gcf(v,s[i])
print(v)