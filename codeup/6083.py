r,g,b=input().split()
r,g,b=int(r),int(g),int(b)
count=0
for i in range(0,r):
    for j in range(0,g):
        for z in range(0,b):
            print(i,j,z)
print(r*g*b)