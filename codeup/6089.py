a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
result=a
for x in range(c-1):
    result=result*b

print(result)