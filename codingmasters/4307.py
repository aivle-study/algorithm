n,m=map(int,input().split())
cost=[]
for i in range(n):
    a=int(input())
    cost.append(a)
cost.sort(reverse=True)
#print(cost)
count=0
while True:
    for i in range(n):
        if cost[i]<=m:
            m-=cost[i]
            count+=1
    break
print(count)