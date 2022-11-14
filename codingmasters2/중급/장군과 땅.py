def such(maps,x,y,visi,point):
    visi.append([x,y])
    point.append(maps[x][y])
    if len(visi)==4:return 0
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]
    maxnum=0
    maxx=0
    maxy=0
    for xx,yy in zip(xl,yl):
        if x+xx>=0 and x+xx<n and y+yy>=0 and y+yy<m:
            if [xx+x,y+yy] not in visi:
                if maxnum<maps[x+xx][y+yy]:
                    maxnum=maps[x+xx][y+yy]
                    maxx=xx+x
                    maxy=yy+y
    such(maps,maxx,maxy,visi,point)

n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))

maxpoint=0

for x in range(n):
    for y in range(m):
        visi=[]
        point=[]
        such(maps,x,y,visi,point)
        if maxpoint<sum(point):
            maxpoint=sum(point)
print(maxpoint)