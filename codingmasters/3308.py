N=int(input())
a=N//4
if N%4>=2:
    b=N//4+1
else:
    b=N//4
print(a*b)