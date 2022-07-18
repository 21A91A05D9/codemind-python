a=int(input())
s=list(map(int,input().split()))
b=int(input())
v=list(map(int,input().split()))
if sorted(s)==sorted(v):
    print("True")
else:
    print("False")