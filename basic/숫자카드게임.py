N,M=input().split()
N,M=int(N),int(M)
lists=[]
for x in range(N):
    arr=input().split()
    arr=list(map(int,arr))
    lists.append(min(arr))
print(max(lists))