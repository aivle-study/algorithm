import re
s = input()
num = re.findall('\d', s)
char = re.sub('[0-9]', '', s)
num = list(map(int, num))
print(*sorted(char), sum(num), sep='')