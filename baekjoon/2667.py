# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기
# 1 : 집이 있는곳, 0 : 집이 없는곳
# dfs
# bfs가 수행속도가 더 빠름
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global count
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        count+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 단지수
result=0
num=[]
count=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            num.append(count)
            count=0
            result+=1

print(result)
num.sort()
for i in num:
    print(i) 