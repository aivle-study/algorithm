k=int(input())
if k%2==1:
    print(k+1)
else:
    while (k/2)%2!=0:
        k+=1
    print(k)