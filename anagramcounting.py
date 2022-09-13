import math
import sys

def solution():
    for i in sys.stdin:
        line = i.split()[0]
        seen = []
        for i in range(0, len(line)):
            if line[i] not in seen:
                seen.append(line[i])
        sol = math.factorial(len(line))
        for s in seen:
            sol = sol // math.factorial(line.count(s))
        print(sol)
        
solution()