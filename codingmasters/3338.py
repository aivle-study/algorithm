def ret(num,le):#[0,261416,2,3]
    if le==1:
        return num
    result=[0,0,0,0]
    dicer2={1:[2,2,3],2:[1,1,2,2,3],3:[1,1,1,1,2,2,2,2]}
    dicer3={1:[1,1,1,2,2],2:[1,1,2],3:[]}
    for x in range(1,3+1):#받아온 1번 2번 3번 각개수 가져오기
        if le==2:
            for c in dicer2[x]:
                result[c]+=num[x]
        if le==3:
            for c in dicer3[x]:
                result[c]+=num[x]
            
    return result

N=int(input())
arr=input().split()
arr=list(map(int,arr))
good=0
sums=[]

sums=[0,1,0,0]
for o in arr:
    sums=ret(sums,o)
good+=sum(sums)*4

sums=[0,0,1,0]
for o in arr:
    sums=ret(sums,o)
good+=sum(sums)*4
 
sums=[0,0,0,1]
for o in arr:
    sums=ret(sums,o)
good+=sum(sums)
good=good%1000000007
print(good)
