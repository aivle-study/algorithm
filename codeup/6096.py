d=[]
for i in range(19):
    x=input().split()
    d.append(list(map(int,x)))

# d = [[0 for j in range(19)] for i in range(19)]
dumi=int(input())

for x in range(dumi):
    a,b=input().split()
    a=int(a)-1
    b=int(b)-1
    for i in range(19):
        if d[a][i]==0:
            d[a][i]=1
            continue
        if d[a][i]==1:
            d[a][i]=0
    for i in range(19):
        if d[i][b]==0:
            d[i][b]=1
            continue
        if d[i][b]==1:
            d[i][b]=0


for x in d:
    for i in x:
        print(i,end=" ")
    print()