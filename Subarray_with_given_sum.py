n=int(input())
while n:
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    v=0
    for i in range(0,a):
        k=0
        for j in range(i,a):
            k+=s[j]
            if k==b:
                print(i+1,j+1)
                v=1
                break
            elif k<b:
                continue
            else:
                break
        if v==1:
            break
    if v==0:
        print("-1")
    n-=1
                
            
            