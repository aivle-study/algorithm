from collections import Counter
n=int(input())
shoe=[]
for i in range(n):
    shoe.append(input())
print((Counter(shoe)).most_common(1)[0][0])

