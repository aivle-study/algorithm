lens,n=input().split()
lens,n=int(lens),int(n)
road=[]
grap=[[]for x in range(lens)]

for i in range(n):
    S,D = map(int, input().split())
    grap[S-1].append(D-1)
    grap[D-1].append(S-1)

for x in grap:
    if len(x)==0:
        print('no')
    else:
        for y in sorted(x):
            print(y+1,end=" ")
        print()