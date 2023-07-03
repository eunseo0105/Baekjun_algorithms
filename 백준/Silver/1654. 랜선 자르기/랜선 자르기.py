import sys

K, N = map(int,sys.stdin.readline().split())
row = []
for i in range(K):
    row.append(int(sys.stdin.readline()))

start, end = 1, max(row)

# 이분 탐색
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in row:
        total += i // mid
    if total >= N:
        start = mid+1
    else:
        end = mid - 1
print(end)