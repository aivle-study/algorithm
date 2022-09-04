from itertools import combinations
from collections import Counter

num = input()
num_list = list(combinations(num, 2))
ans = 'NO'

for i in range(len(num_list)):
    sum1 = sum(map(int, num_list[i]))
    sum2 = sum(map(int, list((Counter(num)-Counter(num_list[i])).elements())))
    if sum1 == sum2: ans = 'YES'
        
print(ans)