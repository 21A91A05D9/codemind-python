n=int(input())
a=n*n
b=str(n)[::-1]
b=int(b)
b=b*b
b=str(b)
if a==int(b[::-1]):
    print("True")
else:
    print("False")