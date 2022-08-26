#각 글자에 해당하는 숫자 세기 -> 차이가 심한 아이 -> 곱해서 확인
from re import T
import numpy as np
A=list(input())
B=list(input())
A2=[]
B2=[]

for i in range(len(A)):
    A2.append([A[i],(A.count(A[i]))])
for i in range(len(B)):
    B2.append([B[i],(B.count(B[i]))])
B2=list(set([tuple(t) for t in B2]))
index=0
index2=0
min=B2[0][1]-A2[0][1]
for i in range(len(A2)):
    for j in range(len(B2)):
        if A2[i][0]==B2[j][0]:
            check=B2[j][1]-A2[i][1]
            if min<=check:             
                min=check
                index=i
                index2=j
a=A2[index][1]
b=B2[index2][1]
count=0
while True:
    # print(a,b)
    if a*2<=b:
        count+=1
        a=a*2
    elif a*2>b:
        count+=1
        break
print(count)
# 2,3,5