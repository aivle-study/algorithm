def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            lit.append(d)
            x = x / d
        else:
            d = d + 1
n=int(input())
cnt=0
for x in range(6,n+1):
    lit=[]
    factorization(x)
    if len(lit)==2:
        if len(set(lit))!=1:
            cnt+=1
print(cnt)