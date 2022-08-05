a,b=input().split()
a=int(a)
b=int(b)
d = [[0 for j in range(b)] for i in range(a)]

dumi=int(input())

for x in range(dumi):
    l,d,x,y=input().split()
    l,d,x,y=int(l),int(d),int(x)-1,int(y)-1
    d[x][y]=1
    if d==1:
        for i in range(1,l+1):
            d[x][y+i]=1
    if d==0:
        for i in range(1,l+1):
            d[x+i][y]=1

for x in d:
    for i in x:
        print(i,end=" ")
    print()