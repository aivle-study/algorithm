from itertools import permutations,combinations
n=int(input())
a=list(map(int,input().split(' ')))
sort_a=sorted(a)
check=list(range(0,len(a)))
x=list(combinations(check,2))
for i in range(len(x)):
    y=a[x[i][0]:x[i][1]]
    print(y)
    y=sorted(y)
    print(y)
    z=a[:[i][0]]+y+a[x[i][1]:]
    print(z)
    if sort_a==z:
        print(x[i][1]-x[i][0])
          