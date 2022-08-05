a = input()
b = ord('a')

while True:
    print(chr(b), end = ' ')
    
    if (chr(b) == a):
        break
    
    b = b + 1
