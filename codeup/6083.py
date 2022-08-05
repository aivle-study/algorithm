a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
count=0
for x in range(a):
    for y in range(b):
        for z in range(c):
            print(x,y,z)
print(a*b*c)
