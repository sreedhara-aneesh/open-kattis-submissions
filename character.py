import math

def solution():
    n = int(input().split()[0])
    r = 0
    for i in range(1, n):
        r += math.comb(n, i + 1)
    print(r)

solution()