n=input()
arr=sorted((map(int,input().split())),reverse=True)
a=arr[0]*arr[1]*arr[2]
b=arr[0]*arr[1]
c=arr[-1]*arr[-2]
d=arr[-1]*arr[-2]*arr[0]
print(max([a,b,c,d]))