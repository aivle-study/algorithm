n=int(input())
lows=[]
age=[]
for x in range(n):
    a,b=input().split()
    a=int(a)
    age.append(a)
    lows.append([a,b])

for ag in sorted(set(age),reverse=True):
    for x in lows:
        if x[0]==ag:
            print(x[1])
