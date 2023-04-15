import math

N, r, c= map(int,input().split())
q=0

def z(N,r,c):
    global q
    half = int(math.pow(2, N-1))
    #1사분면
    if r < half and c < half:
        quad = 1
    #2사분면
    elif r < half and c >= half:
        quad = 2
        c -= half
    #3사분면
    elif r >= half and c < half:
        quad = 3
        r -= half
    #4사분면
    elif r >= half and c >= half:
        quad = 4
        c -= half
        r -= half

    q += half*half * (quad-1)
    N -= 1
    if N == 0:
        return q
    return z(N,r,c)

z(N,r,c)
print(q)
