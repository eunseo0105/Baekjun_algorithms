result = []

for i in range(10000):
    result.append(i)
# a가 9972이면 9999
for i in range(9973):
    sum = 0
    if i < 10:
        sum = i + i
        result.remove(sum)
    elif 9 < i < 100:
        sum = i + (i//10)%10 + (i % 10)
        result.remove(sum)

    elif 99<i<1000:
        sum = i + (i//100) % 10 + (i//10) % 10 + (i % 10)
        if sum in result:
            result.remove(sum)
        else:
            continue

    elif 999<i<10000:
        sum = i + (i//1000)%10 + (i//100)%10 + (i//10) % 10 + (i % 10)
        if sum in result:
            result.remove(sum)
        else:
            continue

for i in result:
    print(i)