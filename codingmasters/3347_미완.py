from distutils.cmd import Command


def movehead(head,dire,command):
    if command=='F':
        if dire==1:
            head[1]+=1
        if dire==2:
            head[0]+=1
        if dire==3:
            head[1]-=1
        if dire==4:
            head[0]-=1
    if command=='R':
        if dire==1:
            head[0]+=1
        if dire==2:
            head[1]-=1
        if dire==3:
            head[0]-=1
        if dire==4:
            head[1]+=1
    if command=='L':
        if dire==1:
            head[0]-=1
        if dire==2:
            head[1]+=1
        if dire==3:
            head[0]+=1
        if dire==4:
            head[1]-=1
    return head
# N,dumi=input().split()
# N=int(N)
# arr=input()
# commands=input()
N=30
arr='abcdefghijklmnopqrstuvwxyzabcd'
commands='RRRRRRRRRRRR'
arr=arr[::-1]
heads=[0,0]
tail=[]
for x in range(-N,0):
    tail.append([0,x])

#머리방향 1:위 2:오른 3:아래 4:왼
dires=2
for x in commands:
    tail.append(heads.copy())
    heads=movehead(heads,dires,x)
    if x=='R':dires+=1
    if x=='L':dires-=1
    if dires==0:dires=4
    if dires==5:dires=1
tail.append(heads.copy())
lasttail=tail[-N:].copy()
snake=[]
tails=lasttail.copy()

for y in range(N):
    maxy=-40
    minx=40
    findex=[]
    for x in tails:
        if x[1] ==maxy:
            findex.append(x)
        if x[1] > maxy:
            findex=[]
            maxy=x[1]
            findex.append(x)
    if len(findex) > 1:
        for x in findex:
            if x[0] ==minx:
                err=1
                errx=x
            if x[0] < minx:
                err=0
                minx=x[0]
                minxindex=x
        snake.append(lasttail.index(minxindex))
        tails.pop(tails.index(minxindex))
        if err==1:
            snake.append(lasttail.index(errx))
    else:
        snake.append(lasttail.index(findex[0]))
        tails.pop(tails.index(findex[0]))

print(lasttail)
for x in snake:
    print(arr[x],end="")

