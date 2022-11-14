def killchain(y):
    for x in grp[y]:
        killapple[x]=1

n=int(input())
dang=list(map(int,input().split()))
dangaplist=[]
for x in range(n):
    dangaplist.append([dang[x],x])
killapple=[0]*n
grp=[[]for _ in range(n)]
for x in range(n-1):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    grp[a].append(b)
    grp[b].append(a)

mxdang=sorted(dangaplist,reverse=True)
for x,y in mxdang:
    if killapple[y]==0:
        nbh=[]#주변사과당도
        for z in grp[y]:#z:y사과에 연결된사과인덱스
            if killapple[z]==0:#연결된사과가 죽었는지 확인
                nbh.append(dang[z])#안죽었으면 nbh에 연결된사과당도 append
        if len(nbh)==1:
            if dang[y]>sum(nbh):
                killchain(y)

msdang=sorted(dangaplist)
for x,y in msdang:#당도가 작은순으로 x:당도 y:인덱스(몇번사과인지)
    if killapple[y]==0:
        nbh=[]#주변 사과 당도
        for z in grp[y]:#z:y사과에 연결된사과인덱스
            if killapple[z]==0:#연결된사과가 죽었는지 확인
                nbh.append(dang[z])#안죽었으면 nbh에 연결된사과당도 append
        if len(nbh)>1:#연결된 안죽은사과가 2개이상일시
            if dang[y]<=sum(nbh):#주변당도 합보다 작을시 사망
                killapple[y]=1
            else:
                killchain(y)#주변당도합보다 클시 주변사과 킬

mxdang=sorted(dangaplist,reverse=True)
for x,y in mxdang:
    if killapple[y]==0:
        nbh=[]#주변사과당도
        for z in grp[y]:#z:y사과에 연결된사과인덱스
            if killapple[z]==0:#연결된사과가 죽었는지 확인
                nbh.append(dang[z])#안죽었으면 nbh에 연결된사과당도 append
        if len(nbh)==1:
            if dang[y]>sum(nbh):
                killchain(y)

# print("ka",killapple)
# print("dang",dang)

sumdang=0
for x,y in zip(killapple,dang):
    if x==0:
        sumdang+=y
print(sumdang)