n=input()
a=['a','e','i','o','u']
b=['A','E','I','O','U']
v=''
for i in n:
    if i in a:
        a.remove(i)
    elif i in b:
        b.remove(i)
if len(a)==0 or len(b)==0:
    print("True")
else:
    print("False")