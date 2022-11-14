a,b=map(int,input().split())
n,m=map(int,input().split())
cost=[int(input()) for _ in range(n)]
cost.sort(reverse=True)
check=0
sum=a
for i in range(m):
    check+=cost[i]
    
print(sum+b*check)