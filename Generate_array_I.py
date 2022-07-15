n=int(input())
s=list(map(int,input().split()))
for i in range(0,len(s),+2):
    t=s[i+1]
    for j in range(t):
        print(s[i],end=" ")