# 거스름돈
n=1260
count=0
coin=[500,100,50,10]
for coin in coin:
    count+=n//coin
    n%=coin
print(coin)
    