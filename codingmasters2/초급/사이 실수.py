a,b=input().split()
a,b=int(a.replace('.',"")),int(b.replace('.',""))
for x in range(a,b+1):
    print(str(x//100)+"."+str(x)[1:],end=" ")