N=int(input())
obj=[]
for x in range(N):
    a,b,c=input().split()#우선순위,가격,거리
    a,b,c=int(a),int(b),int(c)
    obj.append([a,b,c,x+1])


for y in range(N):
    for x in range(N-1):
        if obj[x][2]>obj[x+1][2]:
            obj[x],obj[x+1]=obj[x+1],obj[x]

for y in range(N):
    for x in range(N-1):
        if obj[x][1]>obj[x+1][1]:
            obj[x],obj[x+1]=obj[x+1],obj[x]


for y in range(N):
    for x in range(N-1):
        if obj[x][0]<obj[x+1][0]:
            obj[x],obj[x+1]=obj[x+1],obj[x]

for x in obj:
    print(x[-1],end=" ")