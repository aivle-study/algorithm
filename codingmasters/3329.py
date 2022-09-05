
maps=[]
for x in range(10):
    arr=list(input())
    arr=list(map(int,arr))
    maps.append(arr)
cong=[]
for x in range(10):
    for y in range(10):
        if maps[x][y]==2:
            cong=[x,y]

up=1
yes=0
for x in range(50):
    if cong[0] <=0 or cong[1]<=0:
        yes=1
        break
    if up==1:
        if maps[cong[0]-1][cong[1]]==1:
            up=0
        else:
            cong[0]-=1
    else:
        if maps[cong[0]][cong[1]-1]==1:
            up=1
        else:
            cong[1]-=1

if yes==1:
    print("yes")
else:
    print("no")
