import sys

N, L = map(int, sys.stdin.readline().split())

waterbomb = list(map(int, sys.stdin.readline().split()))
waterbomb.sort()

checkarr = [0] * (max(waterbomb) + 1)
count = 0

for i in waterbomb:
    checkarr[i] = "check"
for i in range(len(checkarr)):
    # print("i", i)
    if checkarr[i] == "check":
        for j in range(i, i + L):
            # print("i + L", i + L)
            # print("j", j)
            if j <= len(checkarr) - 1:
                if checkarr[j] == "check":
                    checkarr[j] = "ok"
                    # print(checkarr)
            elif j >= len(checkarr):
                # print("true", j)
                break
        count += 1
        # print(count)
    continue

print(count)