import itertools
N=int(input())
arr=input().split()
arr=list(map(int,arr))
yes=0
ncr=itertools.permutations(arr,4)
for x in ncr:
    x=list(x)
    if x[0]*x[1]==x[2]*x[3]:
        yes=1
        break

print('YES' if yes==1 else "NO")