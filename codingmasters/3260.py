k = int(input())

while True:
    k += 1
    if k % 2 == 0:
        if (k // 2) % 2 == 1: break
            
print(k)