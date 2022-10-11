import sys

line = input().split()

l, d, n = int(line[0]), int(line[1]), int(line[2])

pos = []
for i in range(0, n):
    pos.append(int(input()))
pos.sort()

# 6 -> b1 -> b2 -> ... -> bn -> l-6
pos.insert(0, 6 - d)
pos.append(l - 6 + d)

add_birds = 0

for i in range(0, len(pos) - 1):
    interval = (pos[i + 1] - d) - (pos[i] + d)
    if interval < 0: 
        continue
    add_birds += (interval // d) + 1

print(add_birds)