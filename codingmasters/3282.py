N,M=input().split()
N,M=int(N),int(M)
maps=[]
for x in range(N):
    arr=input().split()
    arr=list(map(int,arr))
    maps.append(arr)

maxscore=0
for x in range(N):
    for y in range(M):
        score=0
        if x+1<N:
            score+=maps[x+1][y]
        if x-1>=0:
            score+=maps[x-1][y]
        if y+1<M:
            score+=maps[x][y+1]
        if y-1>=0:
            score+=maps[x][y-1]
        score+=maps[x][y]
        if score > maxscore:
            maxscore=score
print(maxscore)
