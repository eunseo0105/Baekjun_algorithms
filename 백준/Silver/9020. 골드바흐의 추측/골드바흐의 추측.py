def GoldBach():
    check = [False, False] + [True] * 10000

    for i in range(2, 101):
        for j in range(i + i, 10001, i):
            check[j] = False

    n = int(input())
    for z in range(n):
        m = int(input())

        a = m // 2
        b = a

        for _ in range(5000):
            if check[a] and check[b]:
                print(a, b)
                break
            a -= 1
            b += 1


GoldBach()