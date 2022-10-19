import sys

# use shoelace algorithm to find area of a polygon

def solution(n):
    points = []
    for i in range(0, n):
        line = input().split()
        points.append([int(line[0]), int(line[1])])
    area = 0
    for i in range(0, len(points)):
        area += determinant(points[i], points[(i + 1) % len(points)]) / 2
    print(f"{'CCW' if area > 0 else 'CW'} {abs(area)}")

def determinant(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

for i in sys.stdin:
    line = i.split()
    n = int(line[0])
    if n == 0: 
        break
    solution(n)