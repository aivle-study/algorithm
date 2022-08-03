"""
a, b, c = map(int,input().split())
p = a+b+c
print(p, round((a+b+c)/3,2))
"""
a, b, c = map(int, input().split())
print (a+b+c, format((a+b+c)/3,'.2f'))