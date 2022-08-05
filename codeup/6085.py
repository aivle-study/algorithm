w, h, b = map(int, input().split())
v = w*h*b/8/1024/1024
print(f'{v:.2f} MB')
# round를 쓰면 0.000...일 때, 0.0까지밖에 출력이 안된다!