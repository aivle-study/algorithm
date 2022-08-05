n = int(input())
r = list(map(int, input().split()))
minimum = r[0]

for i in range(len(r)):
    if minimum > r[i]: minimum = r[i]
print(minimum)
# 코드 길이:151 byte(s) / 수행 시간:15 ms / 메모리 :27724 kb