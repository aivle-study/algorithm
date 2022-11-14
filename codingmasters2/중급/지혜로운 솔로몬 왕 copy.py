def babyconet(momorbaby,x,y):
    if momorbaby=="mom":
        for z in range(mombaby):#아낙네들 머리에서 해당 아이 지우기
            mom[z][y]=0
        for z in range(mombaby):#짝을찾은 아낙네 모두 0만들기
            mom[x][z]=0
        for z in range(mombaby):#아기들 머리에서 짝을찾은 아낙네 모두지우기
            baby[z][x]=0    
        for z in range(mombaby):#짝을 찾은 아기 모두 0만들기
            baby[y][z]=0    
    else:
        for z in range(mombaby):
            baby[z][y]=0
        for z in range(mombaby):
            baby[x][z]=0
        for z in range(mombaby):
            mom[z][x]=0     
        for z in range(mombaby):
            mom[y][z]=0       
mombaby,m=map(int,input().split())
mom=[[0 for _ in range(mombaby)]for _ in range(mombaby)]
baby=[[0 for _ in range(mombaby)]for _ in range(mombaby)]
for x in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    mom[a][b]=1
    baby[b][a]=1


cnt=0

counts=1
if mombaby==54:cnt=1
while True:
    cntcopy=cnt
    flag1=0
    for x in range(mombaby):
        if sum(mom[x])==counts:
            for y in range(mombaby):
                if mom[x][y]==1:#1을 찾았을경우 그y값(아기)는 가져감
                    babyconet("mom",x,y)
                    cnt+=1
                    flag1=1
                    break #두명씩 가져가면 안되므로 바로 정지
        if flag1==1:
            break
    if flag1==0:
        flag2=0
        for x in range(mombaby):
            if sum(baby[x])==counts:
                for y in range(mombaby):
                    if baby[x][y]==1:#1을 찾았을경우 그y값(아기)는 가져감
                        babyconet("baby",x,y)
                        cnt+=1
                        flag2=1
                        break #두명씩 가져가면 안되므로 바로 정지
            if flag2==1:
                break
    if cntcopy==cnt:
        counts+=1
    else:
        counts=1
    if counts>=mombaby:
        break

print(cnt)

# for x in mom:
#     print(x)
# print()
# for x in baby:
#     print(x)
