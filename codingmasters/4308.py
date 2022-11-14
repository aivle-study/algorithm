
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(x/2)):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return 0 # 소수가 아님
    return 1 # 소수임
n=int(input())
print(is_prime_number(n)) 