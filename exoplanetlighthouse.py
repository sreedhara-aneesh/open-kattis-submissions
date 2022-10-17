import math

n = int(input().split()[0])

for i in range(0, n):
    line = input().split()
    r, h1, h2 = line
    r, h1, h2 = float(r), float(h1), float(h2)
    h1 = h1 / 1000 # m to km
    h2 = h2 / 1000 # m to km
    theta1 = math.acos(r / (r + h1))
    theta2 = math.acos(r / (r + h2))
    print(((theta1 + theta2) / (2 * math.pi)) * (2 * math.pi * r))