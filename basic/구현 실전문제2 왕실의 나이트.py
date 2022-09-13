# a1 : 1행 a열
# 1. 위아래 1칸 and 좌우 2칸
# 2. 위아래 2칸 and 좌우 1칸
# 행 1 ~ 8, 열 a ~ h

p = input()
x = int(p[1])       # 행
y = ord(p[0])-96    # 열

cnt = 0

if x == 1 or x == 8:
    if y == 1 or y == 8: cnt += 2
    elif y == 2 or y == 7: cnt += 3
    else: cnt += 4
if x == 2 or x == 7:
    if y == 1 or y == 8: cnt += 3
    elif y == 2 or y == 7: cnt += 4
    else: cnt += 6
if x > 2 and x < 7 and y > 2 and y < 7:
    cnt += 8

print(cnt)