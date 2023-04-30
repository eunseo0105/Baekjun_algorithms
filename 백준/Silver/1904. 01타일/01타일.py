import sys

N = int(sys.stdin.readline())
lst = [0] * (N+2)
lst[1] = 1
lst[2] = 2

for i in range(3, N+1):
    lst[i] = (lst[i - 1] + lst[i - 2]) % 15746

print(lst[N])
