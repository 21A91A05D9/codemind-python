s=str(input())
z=0;x=0;c=0;v=0
for i in s:
    if i==" ":
        z+=1
    elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        x+=1
    elif i=='0' or i<='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        c+=1
    else:
        v+=1
print("Vowels:",end=" ");print(x)
print("Consonants:",end=" ");print(v)
print("Digits:",end=" ");print(c)
print("White spaces:",end=" ");print(z)