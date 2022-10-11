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

for i, group in enumerate(groups):
    max_len = 0
    for word in group:
        max_len = max(max_len, len(word))
    for word in group:
        print(str(word[::-1]).rjust(max_len))
    if i != len(groups) - 1:
        print()