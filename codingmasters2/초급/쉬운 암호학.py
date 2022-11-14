def isPrime(N):
    if (N < 2): 
        return False
    for i in range(2,int(N ** 0.5)):
    	if (N%i == 0): 
            return False
    return True

x = int(input())

d = 2
while d <= x:
    if x % d == 0:
        if isPrime(d)==True:
            x = x / d
            if isPrime(x)==True:
                print(d,int(x))
                break
            else:
                print("IMPOSSIBLE")
                break
        else:
            print("IMPOSSIBLE")
            break
    else:
        d = d + 1
