# 행성터널
# n개의 행성
# n-1개의 터널 건설
# cost = min(|a-b|,|a-b|,|a-b|)

#cost 계산
def cost(a,b):
    x1,y1,z1=a
    x2,y2,z2=b
    return min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
n=int(input())
locate=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    locate.append((x,y,z))
    
graph=[]
for i in range(len(locate)):
    for j in range(len(locate)/2):
        c=cost(locate[i],locate[j])
        graph.append((c,i,j))

parent=[0]*(n+1)

#부모는 자기자신
for i in range(1,n+1):
    parent[i]=i
    
graph.sort()
result=0
for g in graph:
    cost,a,b=g
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result) 