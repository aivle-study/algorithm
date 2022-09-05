def air(maps,x,y,B,N):
    for lens in range(1,B+1):
        if x+lens<N:
            maps[x+lens][y]+=1
        if x-lens>=0:
            maps[x-lens][y]+=1
        if y+lens<N:
            maps[x][y+lens]+=1
        if y-lens>=0:
            maps[x][y-lens]+=1
    return maps

N,A,B,C=input().split()
N,A,B,C=int(N),int(A),int(B),int(C)
maps=[[0 for x in range(10)] for x in range(10)]
aircon=[]
for x in range(A):
    x,y=input().split()
    maps=air(maps,int(x)-1,int(y)-1,B,N)
    aircon.append([int(x)-1,int(y)-1])

for x in aircon:
    maps[x[0]][x[1]]=-9

count=0
for x in maps:
    for y in x:
        if y>=C:
            count+=1
print(count)