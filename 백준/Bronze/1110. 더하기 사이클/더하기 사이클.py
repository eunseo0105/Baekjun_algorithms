v = int(input())
x = v
count = 0
for i in range(100):
    a = x // 10
    b = x % 10
    c = (a+b) % 10
    x = b * 10 + c
    count += 1
    if x == v:
        break
        
print(count)