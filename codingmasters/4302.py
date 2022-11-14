n=int(input())
weight=list(map(int,input().split()))
a,b=map(int,input().split())
print(min(weight[a-1:b-1]))