def isPrime(N):
    if (N < 2): 
        return False
    for i in range(2,int(N ** 0.5)):
    	if (N%i == 0): 
            return False
    return True

n=int(input())
print(isPrime(n))