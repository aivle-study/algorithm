N=int(input())
maps=[]

for x in range(N):
    a,b=input().split()
    a,b=int(a),int(b)
    maps.append(list(range(a,b+1)))

maxcount=0
low=30
for x in range(30,-1,-1):
    count=0
    for y in maps:
        if x in y:
            count+=1
        
    if count>=maxcount:
        maxcount=count
        low=x

print(low)
