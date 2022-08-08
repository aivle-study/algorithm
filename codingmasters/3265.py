A, B = map(int, input().split())
l1 = abs(A-B)
l2 = (59-max(A,B)) + min(A, B) + 1
print(l1) if l1 <= l2 else print(l2)