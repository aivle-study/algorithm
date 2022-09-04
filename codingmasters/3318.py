a, b = map(int, input().split())
a_sum, b_sum = 0, 0

for i in range(1,a):
    if a%i==0: a_sum += i        
for j in range(1,b):
    if b%j==0: b_sum += j
        
print('YES') if a_sum == b and b_sum == a else print('NO')