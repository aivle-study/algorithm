n = int(input(), 16) # 16진수
for i in range(1,16):
    # 16진수로 출력하는데 X는 대문자, x는 소문자
    print(f'{n:X}*{i:X}={(n*i):X}')

# 문제에서는 % 포맷팅을 썼지만 나는 f-string이 더 좋다!