d=[]
for x in range(10):
    a=input()
    d.append(list(map(int,a.split())))

x,y=1,1
d[x][y]=9
while True:
    if d[x][y+1]==0:
        y+=1
        d[x][y]=9
        continue
    if d[x+1][y]==0:
        x+=1
        d[x][y]=9
        continue
    if d[x][y+1]==2:
        y+=1
        d[x][y]=9
        break
    if d[x+1][y]==2:
        x+=1
        d[x][y]=9
        break   
    break

for x in range(10):
    for i in range(10):
        print(d[x][i],end=" ")
    print()