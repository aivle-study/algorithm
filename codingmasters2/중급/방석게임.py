import itertools
def bfs(a,b,c,d):
    visited = [[0]*m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = [(a,b)]
    visited[a][b] = 0
    while queue:
        x, y = queue.pop(0)
        if x == c and y == d:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(input()))

clist=[]
plist=[]

for x in range(n):
    for y in range(m):
        if maps[x][y]=='C':clist.append([x,y])
        if maps[x][y]=='P':plist.append([x,y])

clenlist=[]
# print(clist,plist)
for c in clist:
    lists=[]
    for p in plist:
        lists.append(bfs(c[0],c[1],p[0],p[1]))
    clenlist.append(lists)
# print(clenlist)

minest=10000
for x in list(itertools.permutations(range(len(clist)),len(clist))):
    sumli=[]
    for y in range(len(x)):
        sumli.append(clenlist[x[y]][y])
    if minest>max(sumli):
        minest=max(sumli)
print(minest)