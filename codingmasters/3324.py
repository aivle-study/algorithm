N,M,K=input().split()
N,M,K=int(N),int(M),int(K)

nodes=[0]*N
road=[]
for x in range(N):
    nodes[x]=int(input())


for x in range(M):
    a,b=input().split()
    a,b=int(a),int(b)
    road.append([a-1,b-1])

count=0
for le in range(N):
    for x in road:
        diff=nodes[x[0]]-nodes[x[1]]
        if abs(diff) > K:
            if diff<0:
                nodes[x[0]]+=abs(diff)-K
                count+=abs(diff)-K
            else:
                nodes[x[1]]+=abs(diff)-K
                count+=abs(diff)-K

print(count)

