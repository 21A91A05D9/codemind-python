n=int(input())
s=list(map(int,input().split()))
a=int(input())
if a in s:
    print(s.index(a))
else:
    print("-1")