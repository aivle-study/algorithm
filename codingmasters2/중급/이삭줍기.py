n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))
sums=sum(map(lambda x:sum(x),maps))

floursum=[]

for z in range(n-1):
    if z%2==0:
        for x in range(m-1):
            sumfls=sum(maps[z][x+1:])+sum(maps[z+1][:x-m])
            floursum.append(sumfls)
    else:
        for x in range(m-1):
            sumfls=sum(maps[z][:m-x-1])+sum(maps[z+1][m-x:])
            floursum.append(sumfls)

if n%2==0:
    print(sums-min(floursum))
else:
    print(sums)