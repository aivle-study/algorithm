maps=[]
for x in range(5):
    arr=input().split()
    maps.append(arr)

print(maps)
count=0
shapcount=0
for y in range(5):
    for x in range(5):
        if maps[y][x]=='#':
            shapcount+=1
            if y+1<5:
                if maps[y+1][x]=='#':count+=1
            if y-1>=0:
                if maps[y-1][x]=='#':count+=1
            if x+1<5:
                if maps[y][x+1]=='#':count+=1
            if x-1>=0:
                if maps[y][x-1]=='#':count+=1

if count>=6 and shapcount==4:
    print("YES")
else :
    print("NO")