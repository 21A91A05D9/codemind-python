a=int(input())
for j in range(a):
    c=0
    s=str(input())
    n=len(s)
    for i in s:
        if i>='0' and i<='9':
            c+=1
    if c!=n:
        print("False")
    else:
        print("True")