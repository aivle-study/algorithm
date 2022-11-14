n,s,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.append(s)
if len(arr)==2:
    print(arr[1]-arr[0])
elif s>max(arr[:-1]) and n==m and n!=s:
    print(s+max(arr[:-1])-min(arr[:-1]))
elif (sum(arr)%2==0 and n%2==0) or (sum(arr)%2!=0 and n%2!=0):
    print(n)
else:
    print(n-1)