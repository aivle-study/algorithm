# B에 없는 A를 찾아서 A에서 지우고 그 순서를 확인
A=input()
B=input()

# result=A
# for char in A:
#     if char in B:
#         result=result.replace(char,"")
# print(result)
# x=list(result)
# for i in range(len(x)):
#     if x[i] in A:
#         print(A.split(x[i]))
        
# 앞에서 부터 순서대로 하기
# b문자열 첫문자 slicing , find -1 return 

if B[0] in A:
    result=A.find(B[0])
    print(result)
    X=B[result:]
    print(X)