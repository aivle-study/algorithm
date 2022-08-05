a=int(input())

for x in range(1,a+1):
    if(x%10==3 or x%10==6 or x%10==9):
        print("X",end=' ')
    else:
        print(x,end=' ')