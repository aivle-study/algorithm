mombaby,m=map(int,input().split())

momlist=[[x]for x in range(mombaby)]
babylist=[[x]for x in range(mombaby)]
for x in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    momlist[a].append(b)
    babylist[b].append(a)
visit=[0]*mombaby

while len(momlist):
    momlist.sort(key=len)
    babylist.sort(key=len)
    mom=[]
    baby=[]
    while True:
        print(momlist,babylist)
        if len(babylist[0])>len(momlist[0]):
            mom=momlist.pop(0)
            if len(mom)>1:
                break
        else:
            baby=babylist.pop(0)
            if len(baby)>1:
                break

    if len(mom)>len(baby):
        visit[mom[-1]]=1
        for x in range(len(momlist)):
            if mom[-1] in momlist[x]:
                momlist[x].pop(momlist[x].index(mom[-1]))
        for x in range(len(babylist)):
            if mom[-1]==babylist[x][0]:       
                babylist.pop(babylist.index(babylist[x]))
    else:
        visit[baby[-1]]=1
        for x in range(len(babylist)):
            if baby[-1] in babylist[x]:
                babylist[x].pop(babylist[x].index(baby[-1]))
                break
        for x in range(len(momlist)):
            if baby[-1]==momlist[x][0]:       
                momlist.pop(momlist.index(momlist[x]))
                break
        
print(sum(visit))
