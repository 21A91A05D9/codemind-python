n=int(input())
for i in range(0,n):
    s=str(input())
    if any(chr.isdigit() for chr in s):
        print("Yes")
    else:
        print("No")
    