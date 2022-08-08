# 웹 해킹을 공부하던 또리는 ', ", \ (큰따옴표, 작은 따옴표, 백슬래시)가
#  그대로 데이터베이스의 query로 전달되면 위험하다는 걸 깨달았습니다.
# 또리를 위해 주어진 문장의 ', ", \ 를 \', \", \\ 으로 
# 바꾼 문자열을 출력하는 프로그램을 작성해주세요.

# from dataclasses import replace

arr=input()
arr=arr.replace("\\","\\\\").replace("\'","\\\'").replace("\"","\\\"")

print(arr)