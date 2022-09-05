N=int(input())
arr=list(map(int,input().split()))

maxs=0
#arr= 0~9  surch 1~8
for x in range(1,N-1):
    if list(sorted([arr[x-1],arr[x],arr[x+1]]))[1]>maxs:
        maxs=list(sorted([arr[x-1],arr[x],arr[x+1]]))[1]

print(maxs)
