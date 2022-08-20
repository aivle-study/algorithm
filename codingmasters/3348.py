#IoU
n=int(input())
union=0 #합
inter=0 #교
x_a=[]
y_a=[]
w_a=[]
h_a=[]
for i in range(n):
    x,y,w,h=map(int,input().split(" "))
    x_a.append(x)
    y_a.append(y)
    h_a.append(h)
    w_a.append(w)
    
if n==2: #어차피 최대 IoU쌍은 두 개일수밖에
    print("1 2")

    