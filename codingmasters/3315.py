def stempmap(map,A,N,M,o,m,g):
    '''#'c','f','m'
    map:실행할 맵 A:반복횟수 N,M:행,열 o=전파문자 m=감염문자 g=감염대상
    '''
    stempmap=[['0' for col in range(M)] for row in range(N)]
    for rety in range(A):
        ocstemp=stempmap.copy()
        for x in range(N):#근처 1칸 스템프 찍기
            for y in range(M):
                if map[x][y]==o or map[x][y]==m:
                    if x>0:ocstemp[x-1][y]=m
                    if x<(N-1):ocstemp[x+1][y]=m
                    if y>0:ocstemp[x][y-1]=m
                    if y<(M-1):ocstemp[x][y+1]=m
        for x in range(N):#스탬프 적용
            for y in range(M):
                if g=='g':
                    if map[x][y]!=o and ocstemp[x][y]==m:
                        map[x][y]=m
                else:
                    if ocstemp[x][y]==m:
                        map[x][y]=m
    return map


N,M=input().split()
M,N=int(M),int(N)
map=[]
for x in range(N):
    arr=input()
    map.append(list(arr))
A,B=input().split()
A,B=int(A),int(B)

cats=[]
for y in range(M):
    for x in range(N):
        if map[x][y]=='c':
            cats.append([x,y])

stempmap(map,A,N,M,'o','m','g')

for x in cats:
    map[x[0]][x[1]]='c'
stempmap(map,B,N,M,'c','f','m')
count=0
for x in map:
    for y in x:
        if y=='m':
            count+=1
print(count)
for x in map:
    print(x)