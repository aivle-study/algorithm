n=int(input())+1
lie=[0,1]
for x in range(3,n):
    if x%2==0:
        lie.append(x*lie[x-2]+1)
    else:
        lie.append(x*lie[x-2]-1)

print(lie[-1]%10007)