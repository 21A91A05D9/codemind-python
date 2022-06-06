a=input()
a=a.lower()
a=a.split()
k=0
vowels={'a','e','i','o','u'}
for i in a:
    v=0
    if i[0] in vowels:
        v+=1
    if v==1:
        if i[len(i)-1] not in vowels:
            k+=1
print(k)