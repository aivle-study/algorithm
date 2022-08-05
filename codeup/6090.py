a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
result=a
for x in range(d-1):
    result=result*b+c

print(result)