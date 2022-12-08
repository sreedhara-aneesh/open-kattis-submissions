import math

N = int(input().split()[0])

n = N + 1

out = (math.ceil(n / 2) + 1) * math.ceil(n / 2)

if n % 2 != 0:
    out -= math.ceil(n / 2)

print(out)