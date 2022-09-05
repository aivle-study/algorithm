N=int(input())
arr=input().split()
arr=list(map(int,arr))

bad=0
for x in range(1,N+1):
    start=arr.index(x)
    end=arr.index(x,arr.index(x)+1)
    left=arr[start:end]
    if (len(left)-1)//2 != len(list(set(left)))-1:
        bad=1
        break

if bad==0:
    print("YES")
else: 
    print("NO")

