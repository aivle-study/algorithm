N=int(input())
arr=input().split()
arr=list(map(int,arr))
sums=0
for x in set(arr):
    sums+=(arr.count(x)//x)
print(sums)
