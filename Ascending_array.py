n=int(input())
s=list(map(int,input().split()))
v=0
for i in range(n-1):
   if s[i]>=s[i+1]:
       v=1
       print("no")
       break
if v==0:
     print("yes")
       