import sys

n = int(input())
s = sys.stdin.readline().rstrip()
color = [0, 0]

if s[0] == 'R':
    color[0] += 1
else:
    color[1] += 1
for i in range(1, n):
    if s[i] != s[i-1]:
        if s[i] == 'R':
            color[0] += 1
        else:
            color[1] += 1

print(min(color)+1)
