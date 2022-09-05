N1,M1=input().split()
N1,M1=int(N1),int(M1)
grap1=[0]*N1
for x in range(M1):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    grap1[a]+=1
    grap1[b]+=1

grap1=sorted(grap1)

N2,M2=input().split()
N2,M2=int(N2),int(M2)
grap2=[0]*N2
for x in range(M2):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    grap2[a]+=1
    grap2[b]+=1

grap2=sorted(grap2)

if set(grap1)==set(grap2):
    print("YES")
else:
    print("NO")