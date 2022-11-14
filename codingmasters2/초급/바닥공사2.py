from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

@lru_cache(maxsize=100)
def block(n):
    if n==1:
        return 1
    if n==2:
        return 3
    return block(n-1)+block(n-2)*2

n=int(input())
print(block(n)%796796)

