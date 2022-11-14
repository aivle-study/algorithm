import math
Enemynum=int(input())
Enemylist=[]
for x in range(Enemynum):
    Enemylist.append(int(input()))

udt,marin=input().split()
udt,marin=int(udt),int(marin)

sums=0
for x in Enemylist:
    if x-udt<=0:
        sums+=1
        continue
    else:
        sums+=1
        sums+=math.ceil((x-udt)/marin)
print(sums)