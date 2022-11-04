# 배열 돌리기
n=int(input())
array=list(map(int,input().split()))
for x in array:
    print(x,end=' ')
print()
for _ in range(n-1):
    a=array[0]
    array.remove(a)
    array.append(a)
    for x in array:
        print(x,end=' ')
    print(end='\n')