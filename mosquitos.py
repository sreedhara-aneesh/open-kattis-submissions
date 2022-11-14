import math
import statistics

def solution():
    
    line = input().split()
    n, d = int(line[0]), float(line[1])

    r = d / 2

    points = []

    for i in range(0, n):
        line = input().split()
        points.append([float(line[0]), float(line[1])])
    
    maxcaught = 0

    for i1 in range(0, len(points)):
        for i2 in range(i1 + 1, len(points)):
            centers = findhk(points[i1], points[i2], r)
            if centers is None:
                continue
            c1, c2 = centers
            caught = max(numpointsincircle(points, c1, r), numpointsincircle(points, c2, r))
            maxcaught = max(caught, maxcaught)

    print(maxcaught)

def findhk(p1, p2, r):
    d = distance(p1, p2)
    if d > 2*r or d == 0:
        return None
    
    x1, y1 = p1
    x2, y2 = p2

    c1 = x1**2 - x2**2
    c2 = -2*x1 + 2*x2
    c3 = y1**2 - y2**2
    c4 = -2*y1 + 2*y2
    c5 = c1 + c3
    c6 = -1*(c4/c2)
    c7 = -1*(c5/c2)
    c = x1**2 - 2*x1*c7 + c7**2 + y1**2 - r**2
    b = -2*x1*c6 + 2*c6*c7-2*y1
    a = c6**2 + 1

    k1 = (-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    h1 = c6*k1 + c7
    k2 = (-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    h2 = c6*k2 + c7

    return [[h1, k1], [h2, k2]]

def numpointsincircle(points, center, r):
    n = 0
    for p in points:
        d = distance(p, center)
        if d <= r + (10**(-5) / 2):
            n += 1
    return n


def find_mid(locs):
    xs = []
    ys = []
    for loc in locs:
        xs.append(loc[0])
        ys.append(loc[1])
    x = statistics.fmean(xs)
    y = statistics.fmean(ys)
    return [x, y]

def find_2_outliers(locs):
    mid = find_mid(locs)
    idx_1 = 0
    idx_2 = 0
    dist_1 = 0
    dist_2 = 0
    for i in range(0, len(locs)):
        dist = distance(mid, locs[i])
        if dist > dist_1:
            dist_2 = dist_1
            idx_2 = idx_1
            dist_1 = dist
            idx_1 = i
            continue
        if dist > dist_2:
            dist_2 = dist
            idx_2 = i
            continue
    return [idx_1, idx_2]
        


def find_outlier(locs):
    mid = find_mid(locs)
    max_dist = 0
    out_idx = 0
    for i in range(0, len(locs)):
        loc = locs[i]
        dist = distance(mid, loc)
        if dist > max_dist:
            out_idx = i
            max_dist = dist
    return out_idx

def distance(a, b):
    return math.sqrt((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)

n = int(input().split()[0])
for i in range(0, n):
    input()
    solution()