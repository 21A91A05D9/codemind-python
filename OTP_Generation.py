n=int(input())
t=n
l=[]
while t:
    r=t%10
    if r%2!=0:
        r=r*r
        l.append(r)
    t=t//10
a=len(l)
for i in range(a-1,-1,-1):
    print(l[i],end="")