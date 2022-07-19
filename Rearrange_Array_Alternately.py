n=int(input())
while n:
    a=int(input())
    s=list(map(int,input().split()))
    s=sorted(s)
    k=[]
    i=0;j=len(s)-1
    while i<=j:
        if i==j:
            k.append(s[i])
            break
        k.append(s[j])
        k.append(s[i])
        i+=1
        j-=1
    print(*k)
    n-=1