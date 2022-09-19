#부품찾기(p197)
#부품 n개, m개 종류 -> 모두 있는가?
n=int(input())
stock=list(map(int,input().split()))
m=int(input())
cust=list(map(int,input().split()))

#이진탐색
def find(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        print("yes",end=' ')
    elif array[mid]>target:
        return find(array,target,start,end-1)
    elif array[mid]<target:
        return find(array,target,mid+1,end)
#정렬확인
stock.sort()
for i in cust:  
    result=find(stock,i,0,n-1)
    