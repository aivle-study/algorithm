#https://www.acmicpc.net/problem/1613
# 역사
# 일부 사건의 전후 관계 주어짐
# 주어진 사건들의 전후 관계도 알 수 있을까?

# 사건의 개수 n
# 사건의 전후 관계 수 k
# 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s

n,k=map(int,input().split())
graph=[[0]*(n) for _ in range(n)]

for _ in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][a]:
                graph[a][b]=1
                
s=int(input())
for _ in range(s):
    x,y=map(int,input().split())
    if graph[x-1][y-1]==1:
        print(-1)
    elif graph[y-1][x-1]==1:
        print(1)
    elif graph[x-1][y-1]==0:
        print(0)