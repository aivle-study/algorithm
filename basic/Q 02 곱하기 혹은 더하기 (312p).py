s = input()
ans = 0

for i in s:
    if int(i) <= 1 or ans == 0: ans += int(i) 
    # 0,1이면 더하는게 낫고, ans가 0이면 무조건 더하기부터 해야됨
    
    else: ans *= int(i)
        
print(ans)