import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
if n == 1:
    dp[1] = 1
    result = int(dp[1] % 10007)
    print(result)
elif n == 2:
    dp[1] = 1
    dp[2] = 3
    result = int(dp[2] % 10007)
    print(result)
else:
    for i in range(3, n+1):
        dp[1] = 1
        dp[2] = 3
        dp[i] = dp[i-1] + 2 * dp[i-2]
    result = int(dp[n] % 10007)
    print(result)
