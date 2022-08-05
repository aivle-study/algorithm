dumi=input()
a=input().split()
d=list(map(int,a))
res=[0]*23
for x in d:
    res[x-1]+=1

for x in res:
    print(x,end=" ")
