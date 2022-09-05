N,M=input().split()
N,M=int(N),int(M)
arr=[0]*N
for x in range(M):
    C,n=input().split()
    C,n=int(C),int(n)
    price= C//n
    pepel=list(input().split())
    for y in pepel:
        arr[int(y)-1]+=price

for x in arr:
    print(x,end=" ")