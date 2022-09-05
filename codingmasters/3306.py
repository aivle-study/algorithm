def soso(n):
    sosu = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if sosu[i]:
            for j in range(i+i, n+1, i):
                sosu[j] = False

    return [i for i in range(2, n+1) if sosu[i]]
    
N=int(input())
if N==1:
    print(1)
else:
    if N==soso(N)[-1]:
        print('clap')
    else:
        print(N)