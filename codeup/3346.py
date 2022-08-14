import itertools

n = input()
ans = 'NO'
num = ''

for i in itertools.permutations([j for j in n],len(n)):
    num = ''
    for k in range(len(n)):
        num+=i[k]
    if int(num)%13==0: 
        ans='YES'
        break
        
print(ans)