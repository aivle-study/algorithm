#백준
#경로찾기
n=int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(0,n):
    for a in range(0,n):
        for b in range(0,n):
            if graph[a][b]==1 or (graph[a][k]==1 and graph[k][b]==1):
                graph[a][b]=1
        
#print(graph)     
       
for a in range(0,n):
    for b in range(0,n):
        if graph[a][b]==0:
            print(0,end= ' ')
        else:
            print(1,end=' ')
    print()
    
