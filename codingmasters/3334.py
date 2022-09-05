import copy
import random
def road(maps,x,y,arr,N,M):
    xs=x
    ys=y
    maps[x][y]='.'
    maps2=copy.deepcopy(maps)
    for le in range(2000):
        maps=copy.deepcopy(maps2)
        x=xs
        y=ys
        yes=0
        no=0
        for ary in arr:
            no+=1
            move=0
            if y+1<M:
                if maps[x][y+1]==ary:move+=1
            if x+1<N:
                if maps[x+1][y]==ary:move+=4
            if y-1>=0:
                if maps[x][y-1]==ary:move+=7
            if x-1>=0:
                if maps[x-1][y]==ary:move+=15
            if move==5:move=random.choice([1,4])
            if move==8:move=random.choice([1,7])
            if move==16:move=random.choice([1,15])
            if move==11:move=random.choice([4,7])
            if move==19:move=random.choice([4,15])
            if move==22:move=random.choice([7,15])
            if move==12:move=random.choice([1,4,7])
            if move==23:move=random.choice([1,7,15])
            if move==26:move=random.choice([4,7,15])
            if move==27:move=random.choice([1,4,7,15])
            if move==1:
                maps[x][y+1]='.'
                y=y+1
                continue
            if move==4:
                maps[x+1][y]='.'
                x=x+1
                continue
            if move==7:
                maps[x][y-1]='.'
                y=y-1
                continue  
            if move==15:
                maps[x-1][y]='.'
                x=x-1
                continue
            if move==0:
                no-=1
            yes=1
            break
        if no==0:
            break

        if yes==0:
            for ls in range(N):
                for iss in range(M):
                    if maps[ls][iss]!='.':
                        yes=1

        if yes==0:
            return 1
        
    return 0


arr=list(input())
finds=arr[0]
arr=arr[1:]
N,M=input().split()
N,M=int(N),int(M)

maps=[]
for x in range(N):
    ar=list(input())
    maps.append(ar)

count=0

for x in range(N):
    for y in range(M):
        if maps[x][y]==finds:
            maps2=copy.deepcopy(maps)
            count+=road(maps2,x,y,arr,N,M)
            

print(count)