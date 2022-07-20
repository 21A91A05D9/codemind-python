n=int(input())
v=0
while n:
    a=int(input())
    s=list(map(int,input().split()))
    v+=1
    c=0;b=0
    if sorted(s)==s and len(set(s))!=1:
        c=1
    elif sorted(s,reverse=True)==s and len(set(s))!=1:
        c=1
    else:
        for i in range(0,len(s)-1):
            if s[i]>s[i+1] and s[i]>b:
                c+=1
                b=s[i]
        if s[a-1]>b and len(set(s))!=1:
            c+=1
    print("Case #%d:"%v,c)
    n-=1
                