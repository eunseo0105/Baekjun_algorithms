n = int(input())

if n >= 10:
    m = n % 5
    if m == 0:
        sum = 2 + n//5 - 2
    elif m == 1:
        sum = 3 + n//5 - 2
    elif m == 2:
        sum = 4 + n//5 - 2
    elif m == 3:
        sum = 3 + n//5 - 2
    elif m == 4:
        sum = 4 + n//5 - 2
    else :
        sum = -1

else:
    if n == 3 or n == 5:
        sum = 1
    elif n == 6 or n == 8:
        sum = 2
    elif n == 9:
        sum = 3
    else :
        sum = -1

print(sum)