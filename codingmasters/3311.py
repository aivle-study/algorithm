def lendot(a,b,c,d):
    return  (abs(a-c)**2+abs(b-d)**2)**0.5

N,R=input().split()
N,R=int(N),int(R)

maps=[]
for x in range(N):
    x,y=input().split()
    maps.append([int(x),int(y)])

maxx=-100
maxy=-100
minx=100
miny=100
resultx=0
resulty=0
maxs=0
for sni in maps:
    if sni[0]>maxx:maxx=sni[0]
    if sni[1]>maxy:maxy=sni[1]
    if sni[0]<minx:minx=sni[0]
    if sni[1]<miny:miny=sni[0]

for x in range(minx-R,maxx+1+R):
    for y in range(miny-R,maxy+1+R):
        count=0
        for m in maps:
            if lendot(x,y,m[0],m[1])<=R:
                count+=1
        if count>maxs:
            maxs=count
            resultx=x
            resulty=y
        

print(resultx,resulty)


