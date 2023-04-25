n = int(input())
L = []

for i in range(0, n):
    a = int(input())
    L.append(a)


L.sort()
for i in range(0,n):
    print(L[i])



