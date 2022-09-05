arr=input()

for x in range(len(arr)):
    such=arr[:x+1]
    arrs=arr
    for x in range(len(arr)):
        arrs=arrs.replace(such,'~')
    if list(sorted(set(arrs)))[0]=='~':
        print(such)
        break
