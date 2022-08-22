s = input()
search = (s+s).find(s, 1, -1)
print(s) if search == -1 else print(s[:search])