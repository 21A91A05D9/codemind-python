a=int(input())
s=list(map(int,input().split()))
ma=0;c=0
for i in range(a):
    if s[i]==0:
        c=0
    else:
        c+=1
        if c>ma:
            ma=c
print(ma)