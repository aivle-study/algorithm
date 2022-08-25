y, name, yn, stat = input().split()

if int(y) == 0: print(0)
else:
    if stat == 'Officer': print(28)
    else:
        if int(y) >= 5: print(20)
        else:
            if yn == 'N' and name != 'ROKAF': print(32)
            else: print(28)