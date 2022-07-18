n=int(input())
s=list(map(int,input().split()))
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
pa=0
for i in dic:
    pa+=dic[i]//2
print(pa)
    