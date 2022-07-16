n=int(input())
while n>9:
    t=n
    s=0
    while t:
        s=s+(t%10)
        t=t//10
    n=s
print(n)