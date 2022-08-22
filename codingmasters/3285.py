n = int(input())
home = list(map(int, input().split()))
p = [list(map(int, input().split())) for _ in range(n)]

w = []

for i in range(n):
    won = (abs(home[0]-p[i][0]) + abs(home[1]-p[i][1]))*100
    w.append(won)
    
print(min(w))