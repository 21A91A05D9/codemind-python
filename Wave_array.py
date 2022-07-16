n=int(input())
s=list(map(int,input().split()))
c=0;v=0
for i in range(0,n-2,+2):
    if s[i]<s[i+1] and s[i+1]>s[i+2]:
        c+=1
    elif s[i]>s[i+1] and s[i+1]<s[i+2]:
        c+=1
    else:
        v=1
        break
if v==0:
    print("yes")
else:
    print("no")