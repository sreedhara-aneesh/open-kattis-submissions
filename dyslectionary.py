import sys

groups = []
group = []

for i in sys.stdin:

    line = i.split()
    
    if len(line) == 0:
        groups.append(group)
        group = []
        continue

    word = line[0]
    group.append(word[::-1])

groups.append(group)

for group in groups:
    group.sort()

for group in groups:
    for word in group:
        print(word[::-1])
    print()