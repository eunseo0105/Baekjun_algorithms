import random
import sys

lst = []
lst2 = []
lst3 = []

def dwarf():
    global lst2
    lst2 = random.sample(lst, 7)
    if sum(lst2) == 100:
        for j in range(0, 7):
            lst3.append(lst2[j])
        lst3.sort()
        for z in range(0,7):
            print(lst3[z])
    else:
        dwarf()


for i in range(0, 9):
    m = int(sys.stdin.readline().strip())
    lst.append(m)

lst.sort()
dwarf()
