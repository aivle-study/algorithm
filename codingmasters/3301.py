# 군별 육해공군 b
# 연차 현재 - 전역 a
# 신분 간부, 병 d
# 동원지정여부 c 
a,b,c,d=input().split(" ")
a=int(a)
while a>=0 and a<7: #연차는 6이하 양수
    if d=='Private':
        if c=='N':
            if a==0:
                if b=='ROKA'or b=='ROKN'or b=='ROKAF':
                    print(0)
            elif a>=1 and a<=4:
                if b=='ROKA'or b=='ROKN':
                    print(32)
                elif b=='ROKAF':
                    print(28)
            elif a>=5 and a<=6:
                if b=='ROKA'or b=='ROKN'or b=='ROKAF':
                    print(20)
        elif c=='Y':
            if a>=1 and a<=4:
                if b=='ROKA'or b=='ROKN'or b=='ROKAF':
                    print(28)
        break
    elif d=='Officer':
        if a==0 and c=='N' :
            if b=='ROKA'or b=='ROKN'or b=='ROKAF':
                print(0)
        elif a>=1 and a<=6 and b=='ROKA'or b=='ROKN'or b=='ROKAF':
            print(28)
        break
# "6 ROKAF N Officer