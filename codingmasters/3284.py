N=int(input())

cards=[0]
for x in range(1,N+1):
    how=input()
    if how=='D':
        cards.insert(0,x)
    else:
        cards.append(x)

for x in cards:
    print(x,end=' ')