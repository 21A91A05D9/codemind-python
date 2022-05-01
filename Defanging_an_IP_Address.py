s=str(input())
n=len(s)
for i in range(n):
    if s[i]=='.':
        print("[.]",end="")
        continue
    print(s[i],end="")
    