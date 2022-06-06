n=input()
a=list(map(int,input().split()))
c=0;v=0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        v+=1
    elif a[i]<a[i+1]:
        c+=1
if v==c or v-1==c or v==c-1:
    print("yes")
else:
    print("no")