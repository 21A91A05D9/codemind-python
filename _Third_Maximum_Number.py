n=int(input())
s=list(map(int,input().split()))
if n>=3:
    s=set(s)
    s=sorted(s,reverse=True)
    print(s[2])
elif n==2:
    s=sorted(s)
    print(s[1])
else:
    print(*s)
    
    