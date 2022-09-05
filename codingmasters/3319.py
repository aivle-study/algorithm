a,b=input().split()
a,b=int(a),int(b)
N=int(input())
lis=[]
for x in range(N+1):
    lis.append(a*10//b)
    a=(a*10)%b

print(lis)

if lis[-1]>5:
    arr=int("".join(list(map(str,lis[:-1]))))+1
    arr2="0."+str(arr)
else:
    lis=list(map(str,lis[:-1]))
    arr2="0."+"".join(lis)

print(arr2)