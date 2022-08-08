a,b=input().split() #격자크기
a=int(a) 
b=int(b)
d = [[0 for j in range(b)] for i in range(a)]

dumi=int(input())#막대기수

for x in range(dumi):
    l,s,x,y=input().split()
    l,s,x,y=int(l),int(s),int(x)-1,int(y)-1
    d[x][y]=1
    if s==0:
        for i in range(1,l):
            d[x][y+i]=1
    if s==1:
        for i in range(1,l):
            d[x+i][y]=1

for x in d:
    for i in x:
        print(i,end=" ")
    print()