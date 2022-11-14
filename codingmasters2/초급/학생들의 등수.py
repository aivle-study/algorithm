input()
origarr=list(map(int,input().split()))
arr=sorted(origarr,reverse=True)
lists=[]
for x in range(len(arr)):
    lists.append([arr[x],x+1])
for x in range(len(lists)-1):
    if lists[x][0]==lists[x+1][0]:
        lists[x+1][1]-=1
for x in origarr:
    for y in lists:
        if y[0]==x:
            print(x,y[1])
            break