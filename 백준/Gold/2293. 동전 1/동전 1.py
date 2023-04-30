import sys


n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * 10001
dp[0] = 1

for i in coin:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
            # 1: 1
            # 2: 1 1, 2
            # 3: 1 1 1, 1 2
            # 4: 1 1 1 1, 1 1 2, 2 2
            # 5: 1 1 1 1 1, 1 1 1 2, 1 2 2, 5
            # ...

print(dp[k])