arr=input().split()
parr=[]
for x in range(len(arr)):
    if arr[x]=='2':
        if x==0:
            parr.append("L")
        else:
            if parr[x-1]=='L':
                parr.append("R")
            else:
                parr.append("L")
    if arr[x]=="1":
        parr.append("L")
    if arr[x]=='3':
        parr.append("R")

for x in parr:
    print(x,end=' ')