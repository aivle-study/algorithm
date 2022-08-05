dumi=int(input())

d = [[0 for j in range(19)] for i in range(19)]

for x in range(dumi):
    a,b=input().split()
    a=int(a)
    b=int(b)
    d[a-1][b-1]=1


for x in d:
    for i in x:
        print(i,end=" ")
    print()