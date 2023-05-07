import sys

N, K = map(int, sys.stdin.readline().split()) 
lst = list()
for i in range(N):
    lst.append(int(input()))

count = 0

for i in reversed(range(N)):
    count += K//lst[i] 
    K = K%lst[i] 

print(count)