from datetime import datetime
import math

meter = int(input())
N = int(input())
start = sorted([input() for _ in range(N)])
end = sorted([input() for _ in range(N)])

for i in range(N):
    time_1 = datetime.strptime(start[i][5:],"%H:%M:%S")
    time_2 = datetime.strptime(end[i][5:],"%H:%M:%S")
    time_diff = str(time_2 - time_1).split(':')
    hour = int(time_diff[0]) + int(time_diff[1])/60 + int(time_diff[2])/3600
    speed = meter / hour
    print(start[i][:5], math.trunc(speed), sep='')