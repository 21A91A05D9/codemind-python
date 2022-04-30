n=int(input())
ar=list(map(int,input().split()))
s=0
for i in ar:
    if(i%i**0.5==0):
        s=s+i
print(s)