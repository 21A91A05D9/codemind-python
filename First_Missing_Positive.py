n=int(input())
s=list(map(int,input().split()))
for i in range(0,max(s)+2):
    if i not in s and i>0:
        print(i)
        break