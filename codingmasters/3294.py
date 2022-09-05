N=int(input())

win,lose,maxwin,maxlose=0,0,0,0
for x in range(N):
    race=1 if input()=='WIN' else 0
    if race==1:
        win+=1
        lose=0
        if win > maxwin :
            maxwin=win
    else:
        win=0
        lose+=1
        if lose > maxlose:
            maxlose=lose
    print(win,lose,maxwin,maxlose)
