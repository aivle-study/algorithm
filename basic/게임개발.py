def move(maps,x,y,dire):
    dr={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
    back={0:[1,0],1:[0,-1],2:[-1,0],3:[0,1]}
    for co in range(4):
        dire=3 if dire-1==-1 else dire-1
        if maps[x+dr[dire][0]][y+dr[dire][1]] in [1,2]:
            continue
        else:
            maps[x+dr[dire][0]][y+dr[dire][1]]=2
            return maps,x+dr[dire][0],y+dr[dire][1],dire
    if maps[x+back[dire][0]][y+back[dire][1]]==1:
        return maps,x,y,10
    else:
        return maps,x+back[dire][0],y+back[dire][1],dire


#입력
N,M=input().split()
N,M=int(N),int(M)
x,y,dire=input().split()#0북 ,1동 ,2남 ,3서 
x,y,dire=int(x),int(y),int(dire)
maps=[]
for m in range(N):
    arr=input().split()
    arr=list(map(int,arr))
    maps.append(arr)
maps[x][y]=2

#2채우기
while True:
    maps,x,y,dire=move(maps,x,y,dire)
    if dire==10:break
    print(dire)
    for a in maps:
        print(a)
    print()

#2개수 세기
count=0
for a in maps:
    for b in a:
        if b==2:count+=1
print(count)
