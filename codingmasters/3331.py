import copy
N=int(input())-1

star=['*']

for le in range(N):
    newstar=[]
    for x in star:
        arr=''
        arr+=x
        arr+=' '*len(x)
        arr+=x
        newstar.append(arr)
    for x in star:
        arr=''
        arr+=' '*len(x)
        arr+=x
        arr+=' '*len(x)
        newstar.append(arr)
    for x in star:
        arr=''
        arr+=x
        arr+=' '*len(x)
        arr+=x
        newstar.append(arr)
    star=copy.deepcopy(newstar)

for x in star:
    print(x)