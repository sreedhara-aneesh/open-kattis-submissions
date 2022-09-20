# TODO: rewrite because this sucks

import sys

def solution(n):
    matrix = []
    for i in range(0, n):
        line = input().split()
        matrix.append(line)

    chill = []
    for i in range(0, n):
        chill.append(False)

    for i in range(0, n):
        point1 = i
        if chill[point1]:
            continue
        linked1 = getLinked(matrix, point1)
        for j in range(0, len(linked1)):
            point2 = linked1[j]
            linked2 = getLinked(matrix, point2)
            for k in range(0, len(linked2)):
                point3 = linked2[k]
                linked3 = getLinked(matrix, point3)
                for l in range(0, len(linked3)):
                    point4 = linked3[l]
                    if point1 != point2 and point1 != point3 and point2 != point3 and point4 == point1:
                        chill[point1] = True
                        chill[point2] = True
                        chill[point3] = True
    for i in range(0, n):
        if not chill[i]:
            print(i, end=' ')
    print()

def getLinked(matrix = [], point = 0):
    pointRow = matrix[point]
    linked = []
    for i in range(0, len(pointRow)):
        if int(pointRow[i]) == 1:
            linked.append(i)
    return linked
            
for i in sys.stdin:
    line = i.split()
    solution(int(line[0]))