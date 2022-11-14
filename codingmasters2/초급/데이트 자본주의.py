money,man=input().split()
money,man=int(money),int(man)
manlist=sorted(list(map(int,input().split())),reverse=True)

count=0
for mach in manlist:
    if mach <= money:
        count+=1
        money-=mach
print(count)