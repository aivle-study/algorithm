# test case 1개 오류
from typing import Counter
#47, 12, 10, 16, 10, 23, 13, 47, 36, 39, 11, 18, 43, 43, 13, 8, 21, 3, 39, 26, 9, 32, 5, 27, 29, 25, 12, 18, 25, 15, 43, 36, 25, 24, 17, 11, 31, 32, 27, 15, 6, 27, 8, 47, 49, 35, 23, 27, 36, 27
n=int(input())
vote=[]
for i in range(n):
    vote.append(int(input()))
counter=dict(Counter(vote))
counter=list(counter.items())
counter.sort(reverse=True)
find=[]
for i in range(len(counter)-1):
    if counter[i][1]==counter[i+1][1]:
        find.append(counter[i][0])
        find.append(counter[i+1][0])
if len(find)==0:
    counter=dict(counter)
    print(max(counter,key=counter.get))
else: print(min(find))
