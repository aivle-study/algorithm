N=int(input())
arr=[['1']]
for x in range(N-1):
    nexts=[]
    a=sorted(set(arr[x]))
    for y in list(a):
        nexts.append(y)
        nexts.append(str(arr[x].count(y)))
    arr.append(nexts)
print("".join(arr[-1]))