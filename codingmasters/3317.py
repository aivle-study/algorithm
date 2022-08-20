# 0 빈땅, 1 작물, 2 잡초
from itertools import count


n=int(input())
ground=[input() for __ in range(n)]
print(ground)
count=0
# 모든 가로세로에 1이 있는지 체크
for i in range(len(ground)):
    for j in range(n*2,2):
        if '2'in ground[i][j]:
            count+=1
            print(count)
        # if '1' in ground[i][j]: 
        #     print(count)
#print(ground[0][4]) #0 2 4 짝수만 체크