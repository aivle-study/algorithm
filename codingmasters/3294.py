n = int(input())
result = [input() for _ in range(n)]

win_num_now = 0
lose_num_now = 0
win_num_max = 0
lose_num_max = 0

for i in range(n):
    if result[i] == 'WIN':
        win_num_now += 1
        lose_num_now = 0
    else:
        lose_num_now += 1
        win_num_now = 0
        
    if win_num_now > win_num_max:
        win_num_max = win_num_now
    if lose_num_now > lose_num_max:
        lose_num_max = lose_num_now
        
    print(win_num_now, lose_num_now, win_num_max, lose_num_max)