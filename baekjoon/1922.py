# 네트워크 연결

# 모든 컴퓨터 연결
# 최소비용


#특정원소가 속할 집합
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b    
    
n=int(input())
m=int(input())

parent=[0]*(n+1)

#부모는 자기자신
for i in range(1,n+1):
    parent[i]=i

#비용 input
graph=[]
for _ in range(m):
    a,b,cost=map(int,input().split())
    graph.append((cost,a,b))

#최소 비용 계산을 위한 정렬
graph.sort()
result=0
for g in graph:
    cost,a,b=g
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)        