from collections import deque
n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
dq=deque([arr.pop(0)])
while len(arr):
    if len(arr)!=0:
        dq.appendleft(arr.pop(0))
    if len(arr)!=0:
        dq.append(arr.pop(0))

maxs=0
for x in range(1,len(dq)):
    if maxs<abs(dq[x-1]-dq[x]):maxs=abs(dq[x-1]-dq[x])
print(maxs)