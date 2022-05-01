s=str(input())
a=len(s)
sum=0
for i in range(0,a):
    if s[i]>='0' and s[i]<='9':
        sum=sum+int(s[i])
print(sum)
