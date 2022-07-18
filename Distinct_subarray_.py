a=int(input())
b=int(input())
su=0
even=1
odd=0;k=0
for i in range(a,b+1):
    k+=i
    if k%2!=0:
        su+=even
        odd+=1
    else:
        su+=odd
        even+=1
print(su)
        
    