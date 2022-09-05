dumi=int(input())

arr=list(map(int,input().split()))
arr2=sorted(arr).copy()

minx=10
maxx=0

print(arr)
print(arr2)
for x in range(dumi):
    if arr[x]!=arr2[x]:
        if x < minx:
            minx=x
        if x > maxx:
            maxx=x

print(maxx-minx+1)