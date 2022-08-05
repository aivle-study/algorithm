a, b, c = map(int,input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1
print(d)

# 코드 길이:99 byte(s) / 수행 시간:113 ms / 메모리 :27724 kb