#같은 형태 인지 확인
A=(input())
B=(input())
check=[]
check1=[]
check2=[]
# if B==A:
#     print("YES")
# elif (len(set(A))!=len(set(B))): #중복제거한 원소의 수 비교
#     print("NO")
# else:
#     for i in range(len(B)):
#         if B[i]==A[0]: #같은값이면
#             check1=B[i:]
#             check2=B[:i]
#             check=check1+check2
#             if check==A:
#                 print("YES")
#             else:
#                 print("NO")
#                 break
# arr2=arr2[-1]+arr2[:-1]
if B in A*2: print('YES')
else: print('NO')
