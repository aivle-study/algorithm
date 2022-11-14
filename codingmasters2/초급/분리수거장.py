from cmath import inf


n=int(input())
maps=[]
for x in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    maps.append((a,b))

minlen=inf
minap=0
for target in range(n):
    sumlen=0
    for x in range(n):
        sumlen+=abs(maps[target][0]-maps[x][0])*maps[x][1]
    if minlen > sumlen:
        minlen=sumlen
        minap=target

print(minap+1)
