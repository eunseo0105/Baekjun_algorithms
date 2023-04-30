import sys

n = int(sys.stdin.readline())
lst = [0, 1]*n

for i in range(2,n+1):
    lst[i] = lst[i-1]+ lst[i-2]

print(lst[n])
