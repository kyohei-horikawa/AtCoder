from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
MOD = 10**9 + 7

is_safe = [True] * (n + 1)
for i in range(m):
    is_safe[int(input().rstrip())] = False

dp = [0] * (n + 1)
dp[0] = 1
if is_safe[1]:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2, n + 1):
    if is_safe[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] = dp[i] % MOD
    else:
        dp[i] = 0

print(dp[-1])
