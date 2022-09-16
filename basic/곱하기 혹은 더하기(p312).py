#곱하기 혹은 더하기
#가장 큰수 만들기
# 왼쪽에서 순서대로 이루어짐
s=input()
num=list(s)
sum=0
for i in range(len(num)):
    if num[i]==0 or sum==0:
        sum+=int(num[i])
    else:
        sum*=int(num[i])
print(sum)