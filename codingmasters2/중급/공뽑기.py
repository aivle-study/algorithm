n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1=sorted(arr1)
arr2=sorted(arr2)
sums=0
for x,y in zip(arr1,arr2):
    sums+=x*y

print(sums)