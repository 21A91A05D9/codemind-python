n=int(input())
while n!=1 and n!=4 and n>0:
    s=0
    t=n
    while t:
        s=s+pow(t%10,2)
        t=t//10
    n=s
if n==1 or n==7:
    print("True")
else:
    print("False")
    
    