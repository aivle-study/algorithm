n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))
item=[]
d=int(input())
for x in range(d):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    item.append([a,b])

grp=[[10000000 for _ in range(2*n)]for _ in range(2*n)]
#단순 그래프화
for x in range(n*2-2):
    if x%2==0:
        grp[x][x+1]=sum(maps[x//2][1:])
        grp[x][x+2]=maps[x//2+1][0]
    else:
        grp[x][x-1]=sum(maps[(x-1)//2][:-1])
        grp[x][x+2]=maps[(x-1)//2+1][-1]
for x in range(2,n*2):
    if x%2==0:
        grp[x][x+1]=sum(maps[x//2][1:])
        grp[x][x-2]=maps[x//2-1][0]
    else:
        grp[x][x-1]=sum(maps[(x-1)//2][:-1])
        grp[x][x-2]=maps[(x-1)//2-1][-1]
#단순그래프 플로이드 워셜
for k in range(n*2):
    for i in range(n*2):
        for j in range(n*2):
            grp[i][j] = min(grp[i][j], grp[i][k] + grp[k][j])
for x in range(n*2):
    grp[x][x]=0


startx=0
starty=0
hp=maps[0][0]
flag=[0]*10
for x,y in item:
    if startx==x:
        if starty<y:
            left=sum(maps[x][:starty])+grp[x*2][x*2+1]+sum(maps[x][y:-1])
            right=sum(maps[x][starty+1:y+1])
            # print(left,right)
            if left>right:
                flag[0]+=1
            else:
                flag[1]+=1
            hp+=min(left,right)
        else:
            left=sum(maps[x][y:starty])
            right=sum(maps[x][starty+1:])+grp[x*2+1][x*2]+sum(maps[x][1:y+1])
            if left>right:
                flag[2]+=1
            else:
                flag[3]+=1
            # print(left,right)
            hp+=min(left,right)
    else:
        left=sum(maps[startx][:starty])+min((grp[startx*2][x*2]+sum(maps[x][1:y+1])),(grp[startx*2][x*2+1]+sum(maps[x][y:-1])))
        if (grp[startx*2][x*2]+sum(maps[x][1:y+1]))>(grp[startx*2][x*2+1]+sum(maps[x][y:-1])):
            flag[6]+=1
        else:
            flag[7]+=1
        right=sum(maps[startx][starty+1:])+min((grp[startx*2+1][x*2]+sum(maps[x][1:y+1])),(grp[startx*2+1][x*2+1]+sum(maps[x][y:-1])))
        if (grp[startx*2+1][x*2]+sum(maps[x][1:y+1]))>(grp[startx*2+1][x*2+1]+sum(maps[x][y:-1])):
            flag[8]+=1
        else:
            flag[9]+=1

        if left>right:
            flag[4]+=1
        else:
            flag[5]+=1       
        # print(left,right)
        hp+=min(left,right)
    startx=x
    starty=y
print(flag)
print(hp)


# for x in grp:
#     print(x)
# # for x in maps:
#     print(x)
# print(item)