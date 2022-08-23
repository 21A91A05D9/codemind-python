a=input().split()
a=list(a)
v=a[-1]
a=97
while a!=124:
    if chr(a) in v:
        print(chr(a))
        break
    elif chr(a-32) in v:
        print(chr(a-32))
        break
    a+=1