def cola(a):
    if a%2==0:
        print(a,end=" ")
        return cola(a//2)
    else:
        if a==1:
            print(a,end=" ")
            return 1
        print(a,end=" ")
        return cola(a*3+1)
    
n=int(input())
cola(n)