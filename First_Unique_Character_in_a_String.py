s=str(input())
a=len(s)
c=0;p=0
for i in range(a):
    c=0
    for j in range(a):
        if s[i]==s[j]:
            c+=1
    if c==1:
        print(i)
        p+=1
        break
if p==0:
    print("-1")
    