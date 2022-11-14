price,shin=map(int,input().split())
n,m=map(int,input().split())
options=[]
for x in range(n):
    options.append(int(input()))
print(price+shin*sum(sorted(options,reverse=True)[:m]))