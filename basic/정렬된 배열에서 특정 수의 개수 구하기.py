#정렬된 배열에서 특정 수의 개수 구하기(p367)
#n개의 원소, 수열 오름차순 정렬
# X가 등장하는 횟수 
n,m=map(int,input().split())
num=list(map(int,input().split()))

def bin_find(array,target,start,end,count):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            count+=1
            array.remove(target)
            print(count,array)
            return bin_find(array,target,start,end,count)
        if array[mid]>target:
            return bin_find(array,target,start,mid-1,0)
        elif array[mid]<target:
            return bin_find(array,target,mid+1,end,0)
result=bin_find(num,m,0,n-1,0)
if result!=None:
    print(result)
else:
    print(-1)