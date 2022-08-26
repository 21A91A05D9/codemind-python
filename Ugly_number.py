n=int(input())
v=0
while n!=1:
    if n%5==0:
        n=n//5
    elif n%3==0:
        n=n//3
    elif n%2==0:
        n=n//2
    else:
        v=1
        print("Not Ugly Number")
        break
if v==0:
    print("Ugly Number")