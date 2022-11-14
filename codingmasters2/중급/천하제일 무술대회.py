from collections import deque
n=int(input())
man=deque([])
winner=0
loser=[]
for x in range(n):
    name,power=input().split()
    power=int(power)
    man.append([power,name])
    if winner<power:winner=power

while len(man)!=1:
    a=man.popleft()
    b=man.popleft()
    if a[0]<b[0]:
        man.append(b)
        if b[0]==winner:
            loser.append(a[1])
    else:
        man.append(a)
        if a[0]==winner:
            loser.append(b[1])

for x in loser:
    print(x)