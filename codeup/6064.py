a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print(c)
    else:
        print(b)
elif b > a:
    if a > c:
        print(c)
    else:
        print(a)
else:
    if a > b:
        print(b)
    else:
        print(a)
    