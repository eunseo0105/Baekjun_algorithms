import itertools
import sys

answer = 0
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 순열
permu = itertools.permutations(A, n)

for p in list(permu):
    sumNum = 0
    for i in range(n-1):
        sumNum += abs(p[i] - p[i+1])
    if sumNum > answer:
        answer = sumNum

print(answer)