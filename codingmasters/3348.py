N=int(input())
squ=[]

#왼쪽아래 좌표 x,y 오른쪽 위 좌표 x,y 순으로 저장 
for x in range(N):
    sq1=input()
    arr=list(map(int,sq1.split()))
    squ.append([list(range(arr[0],arr[0]+arr[2]+1)),list(range(arr[1],arr[1]+arr[3]+1)),arr[2]*arr[3]])

maxnums=[]
maxnum1=0
maxnum2=0
maxIoU=-1
for x in range(N):
    for y in range(x+1,N):
        webin=set(squ[x][0])&set(squ[y][0])
        highin=set(squ[x][1])&set(squ[y][1])
        inter=(len(webin)-1)*(len(highin)-1)
        unio=squ[x][2]+squ[y][2]
        IoU=inter/unio
        if IoU > maxIoU:
            maxIoU=IoU
            maxnum1=x
            maxnum2=y
            
print(maxnum1+1,maxnum2+1)

