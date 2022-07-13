s=input().split()
v=0;b=0
for i in s:
    v=v+ord(min(i))
    b=b+ord(max(i))
print(abs(v-b))