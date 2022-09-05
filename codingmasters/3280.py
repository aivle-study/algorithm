N=int(input())
dics={}
for x in range(N):
    K,P=input().split()
    dics[K]=P
such=input()
try:
    print(dics[such])
except:
    print(-1)