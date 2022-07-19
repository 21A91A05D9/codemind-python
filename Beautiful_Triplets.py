n=int(input())
s=list(map(int,input().split()))
v=[]
while len(s)!=0:
    c=min(s)
    v.clear()
    for i in s:
        if abs(c-i)!=0:
            v.append(abs(i-c))
    print(len(s))
    s.clear()
    for i in v:
        s.append(i)