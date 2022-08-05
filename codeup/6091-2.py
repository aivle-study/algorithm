a, b, c = map(int,input().split())
for i in range(max(a,b,c), a*b*c+1):
    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break
        
# 코드 길이:155 byte(s) / 수행 시간:93 ms / 메모리 :27724 kb