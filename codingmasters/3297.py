x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

ans = 'NO'

x1_range_min, x1_range_max = x1-r1/2, x1+r1/2
y1_range_min, y1_range_max = y1-r1/2, y1+r1/2

x2_range_min = x2-r2/2
y2_range_min = y2-r2/2

if (x2_range_min <= x1_range_max and x2_range_min >= x1_range_min) and (y2_range_min <= y1_range_max and y2_range_min >= y1_range_min):
    ans = 'YES'

print(ans)