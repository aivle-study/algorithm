from sys import stdin

input = lambda: stdin.readline().strip()


n = int(input()) # 사실상 버리는 입력

numbers = [0, 0, 0, 0, 0, 0, *map(int, input().split()), 0, 0, 0, 0, 0, 0]
n = len(numbers)

total = sum(numbers)

dp = [0 for _ in range(n)]

for i in range(6, n):
    for my_amount, enemy_amount in [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
    ]:
        dp[i] = max(
            dp[i],
            sum(numbers[i - my_amount + 1:i + 1]) + dp[i - (enemy_amount + my_amount)] # 나는 my_amount만큼 먹고
        )

my_score = dp[n - 1]

# 모든 카드 숫자의 합과 내 최고 점수 출력
# print(total, my_score)

print(my_score - abs(total - my_score))