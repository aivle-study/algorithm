N,K=input().split()
N,K=int(N),int(K)

arr=input().split()
arr=list(map(int,arr))
arrs=sorted(list(set(arr)))
carr=arr.copy()
good=0
if K==N:
    print(max(arr))
    good=1
else:
    for x in arrs:
        arr=carr.copy()
        stamparr=carr.copy()
        for y in range(N):
            if arr[y]>=x:
                arr[y]=-1
        for y in range(N):#감염
            if y-1>=0:
                if arr[y-1]==-1:
                    stamparr[y]=-1
                    continue
            if y+1<N:
                if arr[y+1]==-1:
                    stamparr[y]=-1
                    continue
        for y in range(N):
            if stamparr[y]==-1:
                arr[y]=-1
        # print(arr.count(101),arr)
        if arr.count(-1) <= K:
            print(x)
            good=1
            break

if good==0:
    print(1000000000)