n=str(input())
for i in n:
    c=0
    for j in n:
        if i==j:
            c+=1
    if c>1:
        print("False")
        break
if c==1:
    print("True")