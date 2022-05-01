s=input()
a=len(s)
c=0;ma=0
for i in range(0,a-1):
    if s[i]==s[i+1]:
        c+=1
        if c>ma:
            ma=c
    else:
        c=0
print(ma+1)
