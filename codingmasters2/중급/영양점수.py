import itertools

def young(x):
    sums=0
    for re in x:
        for ter in x:
            sums+=foods[re][ter]
    return sums

n=int(input())
foods=[]
for x in range(n):
    foods.append(list(map(int,input().split())))

fdlist=list(range(n))
sun=list(itertools.combinations(range(n),n//2))
minabs=10000
for x in sun[:len(sun)//2]:
    y=list(set(fdlist)-set(x))
    x=list(x)
    xy=young(x)
    yy=young(y)
    if minabs>abs(xy-yy):
        minabs=abs(xy-yy)
    # print(abs(xy-yy))
print(minabs)
