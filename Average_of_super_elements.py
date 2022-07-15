n=int(input())
s=list(map(int,input().split()))
h=0;v=0;l=[]
for i in s:
    if s.count(i)==i and i not in l:
        h=h+i
        v+=1
        l.append(i)
if v!=0:
    h=h/v
    print("%.2f"%h)
else:
    print("-1")