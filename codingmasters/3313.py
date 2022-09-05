def carnum(N):
    N=sorted(N)
    if N[-1]==sum(N[0:4]):return 'YES'
    if N[0]+N[3]==N[1]+N[2]:return 'YEs'
    return 'NO'

N=list(map(int,list(input())))
print(carnum(N))