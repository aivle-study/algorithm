import math
def is_prime(n):
    if n==1:
        return 1
    if n==2 or n==3:
        return 'clap'
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return n
    return 'clap'
        
n=int(input())
print(is_prime(int(n)))
#112,119