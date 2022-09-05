H,W=input().split()
H,W=int(H),int(W)
maps=[]
for x in range(H):
    arr=list(input())
    maps.append(arr)

h,w=input().split()
h,w=int(h),int(w)
masks=[]
for x in range(h):
    arr=list(input())
    masks.append(arr)

for x in range(h):
    for y in range(w):
        if masks[x][y]=='.':
            continue
        else:
            maps[H-h+x][W-w+y]=masks[x][y]

for x in maps:
    for y in x:
        print(y,end="")
    print()