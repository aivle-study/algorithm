n=int(input())
day=input()
d=['MON','TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(d[(d.index(day)+n)%7])
