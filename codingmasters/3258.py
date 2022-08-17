n=int(input())
# 이김 1<2 , 2<3 , 1>3
a_count=0
b_count=0
for i in range(n):
    a,b=map(int,input().split(" "))
    if b!='3' and a>b: # 3>2, 2>1, 
        a_count+=1
        print("q")
    elif a!='3' and b>a: #3>2, 2>1
        b_count+=1
        print("k")
    elif a=='1' and b=='3': # 1>3
        a_count+=1
        print("d")
    elif b=='1' and a=='3':
        b_count+=1
        print("s")
        
        
print(a_count, b_count,sep=" ")