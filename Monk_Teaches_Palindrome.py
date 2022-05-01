a=int(input())
for i in range(0,a):
    c=0
    s=str(input())
    n=len(s)
    j=n-1
    for k in range(0,n):
        if s[k]!=s[j]:
            c+=1
            break
        j-=1
    if c!=0:
        print("NO")
    else:
        if n%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")