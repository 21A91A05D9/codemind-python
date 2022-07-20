n=int(input())
while n:
    a=int(input())
    c=0
    s=list(map(int,input().split()))
    for i in range(len(s)):
        for j in range(len(s)):
            if i!=j:
                su=s[i]+s[j]
                for k in range(len(s)):
                    if su==s[k]:
                        c+=1
    if c==0:
        print("-1")
    else:
        print(c//2)
    n-=1