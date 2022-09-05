arr=input()
N=int(input())
for x in range(N):
    s,t,cur=input().split()
    cur=int(cur)
    arr=arr[:cur]+arr[cur:].replace(s,t)
    print(arr)
