a = int(input())
b = input()

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

idx = day.index(b)+a
print(day[idx%7])