# 도시분할 계획
# n개의 집, m개의 길
# 방향 없음
# 2개의 분리된 마을로 분할
# 경로가 항상 존제
# 나머지 길의 유지비 최소 합

# 크루스칼 알고리즘 : 최소한 비용 신장트리, 모든 정점들을 가장 적은 비용으로 연결
# 즉 모든 정점 포함, 사이클 없음, 가중치 합 최소 -> 크루스칼

#가중치의 오름차순 정렬, 사이클이 형성하지 않는 대로 간선 선택

# 사이클 판단시 union-find 활용
# union-find : 서로소집합을 표현하는 자료구조, union(병합), find

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
    
edges.sort()
last=0

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last=cost
print(result-last)