a=input()
a=a.split()
for i in a:
    ma=max(i)
    mi=min(i)
    ma=ord(ma)
    mi=ord(mi)
    print(ma-mi,end=" ")