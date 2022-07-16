import math
n=int(input())
n=str(n)
s=0
for i in n:
    s=s+int(math.factorial(int(i)))
n=int(n)
if s==n:
    print("The number "+str(n)+" is a strong number")
else:
    print("The number "+str(n)+" is not a strong number")
    