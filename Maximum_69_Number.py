n=int(input())
n=str(n)
l=[]
for i in n:
    l.append(i)
for i in range(len(l)):
    if l[i]=='6':
        l[i]=9
        break
for i in l:
    print(i,end="")
