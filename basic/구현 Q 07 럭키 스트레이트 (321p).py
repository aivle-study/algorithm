score = input()
left = list(map(int, score[0:len(score)//2]))
right = list(map(int, score[len(score)//2:]))
print('LUCKY') if sum(left) == sum(right) else print('READY')