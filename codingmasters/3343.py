import copy
def tailgong(maps,x,y,N,a):
    if x+1<N and a==1:
        if maps[x+1][y]=='.':
            maps[x+1][y]='#'
            return maps,a
    if y+1<N and a==2:
        if maps[x][y+1]=='.':
            maps[x][y+1]='#'
            return maps,a
    return maps,-1

import random
N=int(input())
maps=[]
for x in range(N):
    maps.append(list(input()))
maps2=copy.deepcopy(maps)

lis=[]
for re in range(N*N*1000):
    a=[]
    count=0
    while True:
        for ran in range(N*N//2):
            a.append(random.randint(1,2))

        if "".join(list(map(str,a))) in lis:
            1+2
        else:
            break
    
    maps=copy.deepcopy(maps2)
    arund=''
    nosave=0
    for x in range(N):
        for y in range(N):
            if maps[x][y]=='.':
                if count<len(a):
                    maps,le=tailgong(maps,x,y,N,a[count])
                    count+=1
                    if le==-1:
                        nosave=1
                        break
                    arund+=str(le)
    if nosave==0:
        lis.append(arund)

lis=list(set(lis))
print(len(lis))