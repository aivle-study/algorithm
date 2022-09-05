def suchM(maps,n,m,M):
    result=0
    for x in range(1,M-m):
        if maps[n][m+x]==1:
            result+=1
        else: return result 
    return result

def suchN(maps,n,m,N):
    result=0
    for x in range(1,N-n):
        if maps[n+x][m]==1:
            result+=1
        else: return result
    return result

N,M=input().split()
N,M=int(N),int(M)


maps=[]
for x in range(N):
    arr=list(map(int,list(input())))
    maps.append(arr)


for n in range(N):
    for m in range(M):
        countM=0
        countN=0
        countS=0
        if maps[n][m]==1:
            countM+=suchM(maps,n,m,M)#가로의길이-1
            countN+=suchN(maps,n,m,N)#세로의길이-1
            if countM>0:
                for y in range(0,countM):
                    for x in range(1,countN+1):
                        if suchM(maps,n+x,m,M-y)>=countM-y:
                            countS+=1
                        else: break
            total=countM+countN+countS
            print(countM,countN,countS)
            maps[n][m]+=total


for x in maps:
    print(x)

end=0
for x in maps:
    end+=sum(x)
print(end)
