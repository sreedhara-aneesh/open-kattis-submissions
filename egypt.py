import sys

for i in sys.stdin:
    line = i.split()
    x, y, z = line
    x, y, z = int(x), int(y), int(z)
    if x == 0 and y == 0 and z == 0:
        break
    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        print('right')
    else:
        print('wrong')
