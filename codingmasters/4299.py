# 2개 에러
def mult(arr):
    sum=0
    if len(arr)==1:
        sum=arr[0]
    elif len(arr)==2:
        a=arr[0]
        b=arr[1]
        sum=a*b
    elif len(arr)>=3:
        a=arr[0]
        b=arr[1]
        c=arr[2]
        sum=a*b*c
        if a*b>sum:
            sum=a*b
    return sum

n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
for i in range(n):
    if arr[i]<0:
        minus=arr.index(arr[i])
        break
minus_arr=arr[minus:]
not_minus_arr=arr[:minus]
if 0 in not_minus_arr:
    not_minus_arr.remove(0)
minus_arr.sort()
not_minus_arr.sort(reverse=True)
one=mult(minus_arr)
two=mult(not_minus_arr)
if one>two:
    print(one)
else:
    print(two)

