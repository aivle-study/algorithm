h, m, s = map(int, input().split(':'))
t = int(input())
n = int(input())-1

total = t*n
total_h, total_m, total_s = 0, 0, 0

if total+s >= 60:
    total_m = (total+s)//60
    total_s = (total+s)%60
    if total_m+m >= 60:
        total_h = (total_m+m)//60
        total_m = (total_m+m)%60
        if total_h+h >= 24:
            total_h = (total_h+h)%24
        else: 
            total_h += h
    else: 
        total_m += m
        total_h = h
else:
    total_s = total+s
    total_m = m
    total_h = h

print(f'{total_h:0>2}:{total_m:0>2}:{total_s:0>2}')