a,b=map(int,input().split())
l=[]
for i in range(0,a):
    aa=input().split()
    l.append(aa)
for j in range(0,b):
    s=0
    for i in range(0,a):
        s=s+int(l[i][j])
    print(s,end=" ")
