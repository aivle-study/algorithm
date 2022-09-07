# N 
# 123 402 
n=input()
l=int(len(n)/2)
x=n[:l]
y=n[l:]
x=list(map(int,list(x)))
y=list(map(int,list(y)))
if sum(x)==sum(y):
    print('LUCKY')
else:
    print('READY')

