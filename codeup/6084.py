h, b, c, s = map(int, input().split())
PCM = round(h*b*c*s/8/1024/1024,1)
print(f'{PCM} MB')