arr=str(int(input()))
sums=int(arr[0])
for x in arr[1:]:
    if int(x)==0 or int(x)==1:
        sum+=int(x)
        continue
    else:sums*=int(x)
print(sums)
    