n=int(input())
s=list(map(int,input().split()))
ma=0
for i in range(1,max(s)):
    c=0
    for j in s:
        if j%i==0:
            c+=1
    if c==len(s) and i>ma:
        ma=i
print(ma)
        