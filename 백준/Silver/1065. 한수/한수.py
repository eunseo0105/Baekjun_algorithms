n = int(input())

hansu = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    if i < 100:
        hansu += 1 
    elif a[0]-a[1] == a[1]-a[2]:
        hansu += 1  
print(hansu)