import itertools
def point(a,b,bad,good):
    if ([a,b] in good) or ([b,a] in good):
        return 1
    if ([a,b] in bad) or ([b,a] in bad):
        return -1
    return 0

N=int(input())
K=int(input())
 
stu=[x for x in range(1,N*2+1)]
bad=[]
good=[]
seating=list(itertools.permutations(stu,N*2))
for x in range(K):
    frsh,a,b=input().split()
    a,b=int(a),int(b)
    if frsh=='1':
        good.append([a,b])
    if frsh=='2':
        bad.append([a,b])

maxcount=-100
for set in seating:
    count=0
    for x in range(0,N*2,2):
        count+=point(list(set)[x],list(set)[x+1],bad,good)
    if count>maxcount:
        maxcount=count

print(maxcount)