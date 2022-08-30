n=input().split()
mi=10000
for i in n:
    c=len(i)
    mi=min(mi,c)
print(mi)