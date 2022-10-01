import math
primes=[1 for i in range(1000000)]
def sieve():
    primes[0]=primes[1]=0
    for i in range(2,int(math.sqrt(1000000))+1):
        if(primes[i]==1):
            for j in range(2*i,1000000,+i):
                if(primes[j]==1):
                    primes[j]=0
sieve()
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if primes[i]==1:
        c+=1 
print(c)