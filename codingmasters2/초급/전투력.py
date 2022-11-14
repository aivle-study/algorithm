n=int(input())
marin=sorted(list(map(int,input().split())))
maxattack=0
lens=len(marin)
for x in range(lens):
    if maxattack<(marin[x]*(lens-x)):
        maxattack=(marin[x]*(lens-x))

print(maxattack)