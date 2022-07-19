n=int(input())
s=list(map(int,input().split()))
a=s[0];b=s[0]
for i in range(1,n):
    b=max(s[i],b+s[i])
    a=max(b,a)
print(a)