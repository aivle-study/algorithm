n=int(input())
arr=list(map(int,input().split()))
tori=int(input())
cuts=max(arr)
counts=1
savecuts=0
while True:
    if savecuts==cuts:
        print(cuts)
        break
    savecuts=cuts
    counts*=2
    sums=0
    cnt=0
    for x in arr:
        if x>cuts:
            sums+=cuts
            cnt+=1
        else:
            sums+=x
    if sums<=tori:
        if (tori-sums)<cnt or cuts==max(arr):
            print(cuts)
            break
        else:
            cuts=cuts+max(arr)//counts+1
    else:
        cuts=cuts-max(arr)//counts-1