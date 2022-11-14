n=int(input())
shuse=[]
for x in range(n):
    shuse.append(int(input()))

maxs=0
maxshuse=0
for x in sorted(set(shuse)):
    if maxs<=shuse.count(x):
        maxs=shuse.count(x)
        maxshuse=x

print(maxshuse)

