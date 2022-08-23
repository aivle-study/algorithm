# 0 빈땅, 1 작물, 2 잡초
n=int(input())
ground=[input().split(" ") for __ in range(n)]
print(ground)
check=0 #잡초
for i in range(n):
    for j in range(n):
        if ground[j][i]=='2': 
            check+=1
print(check)
