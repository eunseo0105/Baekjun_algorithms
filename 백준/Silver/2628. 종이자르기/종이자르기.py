
x, y = map(int, input().split())
a = [0, x]
b = [0, y]
n = int(input())


for i in range(1, n+1):
    num, value = map(int, input().split())
    if num == 1:
        a.append(value)

    else:
        b.append(value)

a.sort()
b.sort()

t = []
z = []

for i in range(len(a)-1):
    t.append(a[i+1] - a[i])

for i in range(len(b)-1):
    z.append(b[i+1] - b[i])


print(max(t)*max(z))
















