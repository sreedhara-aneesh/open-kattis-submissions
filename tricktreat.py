import sys
import math

GOLDEN_RATIO = (math.sqrt(5) + 1) / 2

def solution(n):
    points = []
    min_x, max_x = 200000, -200000
    for i in range(0, n):
        raw = input().split()
        point = [float(raw[0]), float(raw[1])]
        min_x, max_x = min(min_x, point[0]), max(max_x, point[0])
        points.append(point)
    # print(points, min_x, max_x)

    def max_dist(x, y=0):
        max_d = 0
        for p in points:
            d = math.sqrt((p[0] - x)**2 + (p[1] - y)**2)
            max_d = max(max_d, d)
        return max_d

    sol = golden_section_search(max_dist, min_x, max_x)
    print(sol, max_dist(sol))
    

# Golden section search algorithm at: 
# https://en.wikipedia.org/wiki/Golden-section_search
def golden_section_search(f, a, b, tol=10**-5):
    c = b - (b - a) / GOLDEN_RATIO
    d = a + (b - a) / GOLDEN_RATIO
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / GOLDEN_RATIO
        d = a + (b - a) / GOLDEN_RATIO
    return (b + a) / 2

for i in sys.stdin:
    line = i.split()
    n = int(line[0])
    if n != 0:
        solution(n)
        input()