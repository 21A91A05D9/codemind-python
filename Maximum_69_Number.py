n=int(input())
n=str(n)
n=list(n)
for i in range(len(n)):
    if n[i]=='6':
        n[i]=9
        break
for i in n:
    print(i,end="")