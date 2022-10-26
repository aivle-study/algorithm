#케빈 베이컨의 6단계 법칙
#최대 6단계 이내에서 서로 아는 사람 연결
# 임의의 두사람이 최소 몇단계 ?
# 케빈 베이컨 수 = 모든 사람과 케빈 베이컨 게임을 했을때 나오는 단계의 합
n,m=map(int,input().split())

#무한
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기자신
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

print(graph)
    