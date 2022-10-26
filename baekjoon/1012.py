# https://www.acmicpc.net/problem/1012
# 유기농 문제
# dfs

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

t=int(input())  
result_list=[]
      
for _ in range(t):
    m,n,k=list(map(int,input().split()))
    
    graph=[[0]*m for i in range(n)]
    
    for i in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1
        
    result=0
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)
    result=0
    
