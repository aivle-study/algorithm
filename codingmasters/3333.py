import copy
import itertools
def sumarr(maps):
    sum=0
    for x in maps:
        for y in x:
            sum+=y
    return sum

N,M,X=input().split()
N,M,X=int(N),int(M),int(X)

maps=[]
for x in range(N):
    arr=input().split()
    arr=list(map(int,arr))
    maps.append(arr)
yes=0
for x in range(N):#행삭제
    rowcom=list(itertools.combinations(range(N),x))
    for r in rowcom:
        maps2=copy.deepcopy(maps)
        for y in list(r):
            maps2[y]=[0]*M 
        for ln in range(M):#열삭제
            lecom=list(itertools.combinations(range(M),ln))
            for l in lecom:
                maps3=copy.deepcopy(maps2)
                for y in list(l):
                    for im in range(N):
                        maps3[im][y]=0
                if sumarr(maps3)==X:
                    yes=1
                    break
                
if yes==1:
    print('YES')
else:
    print("NO")
