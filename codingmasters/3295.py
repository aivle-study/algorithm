import re

cell = input()
col = re.sub('[0-9]', '', cell)
row = re.sub('[A-Z]', '', cell)

if col[-1] == 'A':
    if len(col) == 2:
        col_1 = col[:-2] + 'Z'
    else:
        if col[1] == 'A': 
            if col[0] == 'A': col_1 = 'ZZ'
            else: col_1 = col[0] + 'Z'
        else: col_1 = col[0] + chr(ord(col[1])-1) + 'Z'
else: 
    col_1 = col[:-1] + chr(ord(col[-1])-1)

row_1 = str(int(row) - 1)

print(col_1+row)
print(col+row_1)