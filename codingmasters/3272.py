n = input()
ans = ''

for i in n:
    if i == '3': ans+='clap'
    elif i == '6': ans+='clap'
    elif i == '9': ans+='clap'
    
print(ans) if len(ans)>0 else print(n)