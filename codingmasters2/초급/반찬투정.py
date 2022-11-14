n=int(input())
for x in range(2**n):
    x=format(x,'b')
    print(format(int(x),'0'+str(n)))