n = int(input())
seq = list(map(int, input().split()))
seq_temp = seq.copy()
cnt = []

for i in range(len(seq)):
    if seq[i] == min(seq_temp):
        #print(seq[i], min(seq_temp))
        seq_temp.remove(min(seq_temp))
    else:
        cnt.append(i)
        #print(seq[i], min(seq_temp))
        seq_temp.remove(min(seq_temp))
        
print(len(range(cnt[0],cnt[-1]+1)))