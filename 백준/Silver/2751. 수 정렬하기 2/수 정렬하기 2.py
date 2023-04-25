import sys
n = int(sys.stdin.readline())
L = []

for i in range(0, n):
    a = int(sys.stdin.readline())
    L.append(a)


L.sort()
for i in range(0,n):
    print(L[i])


