n=int(input())
for i in range(n-1,-1,-1):
    t=i
    t=str(t)
    if t==t[::-1]:
        a=i
        break
t=n+1
while t:
    v=str(t)
    if v==v[::-1]:
        b=t
        break
    t+=1
if abs(n-a)==abs(n-b):
    print(a,b)
elif abs(n-a)>abs(n-b):
    print(b)
else:
    print(a)
    
    
    