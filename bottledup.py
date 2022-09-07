def solution():
    line = input().split()
    s = int(line[0])
    v1 = int(line[1])
    v2 = int(line[2])
    amt2 = 0
    while (s % v1 != 0):
        amt2 += 1
        s -= v2
        if (s < 0):
            return None
    return [int(s / v1), amt2]

res = solution()
if not res:
    print("Impossible")
else:
    print(f"{res[0]} {res[1]}")