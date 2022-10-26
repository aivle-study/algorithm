# https://www.acmicpc.net/problem/10159
# 각 문제에 대해서 알수 없는 물건 수 뽑기
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[False]*(N+1) for _ in range(N+1)]
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True

#플로이드 워셜
#k를 거쳐서 가는 경로가 있다면 True
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True

for i in range(1, N+1):
    count = -1
    for j in range(1, N+1):
        #가지도 못하고 오지도 못하면 count+
        if not graph[i][j] and not graph[j][i]:
            count += 1
    print(count)