n=int(input())
arr=input().split()
for x in range(n):
    for y in arr:
        print(y,end=" ")
    print()
    arr.append(arr.pop(0))
