n=int(input())
result=[input() for i in range(n)]
#print(result)
win=0
lose=0
max_w=0
max_l=0
for i in range(len(result)):
    if result[i]=='WIN':
        win+=1
        lose=0
        if win>=max_w:
            max_w=win
        print(win,lose,max_w,max_l,sep=' ')
    elif result[i]=='LOSE':
        lose+=1
        win=0
        if lose>=max_l:
            max_l=lose
        print(win,lose,max_w,max_l,sep=' ')