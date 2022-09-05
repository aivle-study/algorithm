N,M=input().split()#N=구역의 개수
N,M=int(N),int(M)

zone=[0]*N
zone[0]=1
road=[]
for x in range(M):
    s,e=input().split()
    s,e=int(s),int(e)
    road.append([s,e])

for re in range(M-1):
    for x in range(M-1):
        if road[x][0]>road[x+1][0]:
            road[x],road[x+1]=road[x+1],road[x]

for x in road:
    if zone[x[0]-1]==1:
        zone[x[1]-1]=1
good=0
for x in road:
    if x[1]==1 and zone[x[0]-1]==1:
        good=1
if good==1:
    print("YES")
else:
    print("NO")

    