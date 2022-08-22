b = list(map(int, input().split()))

hand = []
temp = 'R'

for i in range(len(b)):
    if b[i] == 1: 
        hand.append('L')
        temp = 'L'
    elif b[i] == 3:
        hand.append('R')
        temp = 'R'
    else:
        if temp == 'R': 
            hand.append('L')
            temp = 'L'
        else:
            hand.append('R')
            temp = 'R'
            
print(*hand)