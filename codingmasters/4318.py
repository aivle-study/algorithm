# 전투력
n=int(input())
power=list(map(int,input().split()))
power.sort(reverse=True)
sum=0
for i in range(len(power)):
        #print(power[0:i+1])
        new_power=power[0:i+1]
        #print(min(new_power)*len(new_power))
        new_sum=min(new_power)*len(new_power)
        if sum<=new_sum:
            #print(sum,new_sum)
            sum=new_sum
print(sum)