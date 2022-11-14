n=int(input())
rows=list(map(int,input().split()))
a,b=map(int,input().split())
print(min(rows[a-1:b]))

