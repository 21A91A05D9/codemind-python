a,b=map(int,input().split())
a=list(map(int,str(a)))
v=a[:b];x=''
for i in v:
    x+=str(i)
x=int(x)
g=a[-b:-1]
h=''
for i in g:
    h+=str(i)
h+=str(a[-1])
h=int(h)
print(abs(x-h))