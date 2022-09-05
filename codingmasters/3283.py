N=int(input())
arr=list(input())
count=0
for x in range(1,N-1):
    if arr[x-1] =='O' and arr[x+1] =='O':
        arr[x-1] ='X'
        arr[x+1] ='X'
        count+=1
count+=arr.count('O')
print(count)