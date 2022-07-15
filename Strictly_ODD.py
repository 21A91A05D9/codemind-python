n=int(input())
s=list(map(int,input().split()))
v=0
for i in range(0,len(s),+2):
    if s[i]%2!=0:
        v+=1
        print("False")
        break
if v==0:
    print("True")
    