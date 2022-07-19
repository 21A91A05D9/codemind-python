n=int(input())
s=list(map(int,input().split()))
l=0;r=1;ma=0;c=0
while r<n:
    if s[l]>s[r]:
        l=r
        r+=1
    else:
        c=abs(s[r]-s[l])
        if c>ma:
            ma=c
        r+=1
print(ma)