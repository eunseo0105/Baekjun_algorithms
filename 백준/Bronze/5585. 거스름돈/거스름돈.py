import sys

n = int(sys.stdin.readline())
N = 1000 - n
count = 0

while N >= 500:
    count += 1
    N = N - 500
while N >= 100:
    count += 1
    N = N - 100
while N >= 50:
    count += 1
    N = N - 50
while N >= 10:
    count += 1
    N = N - 10
while N >= 5:
    count += 1
    N = N - 5
while N >= 1:
    count += 1
    N = N - 1
print(count)

