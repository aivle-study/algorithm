# A명의 적군
# 한명의 특전사는 B명이 적군 상대
# 일반 병사 : C명의 적군 상대
# 최소 군인수?
n=int(input())
army=[]
for a in range(n):
    army.append(int(input()))
b,c=map(int,input().split())
