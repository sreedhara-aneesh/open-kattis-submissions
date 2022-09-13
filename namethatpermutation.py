import math
import sys

def solution(n, k):
    # actual logic
    digs = []
    for i in range(0, n):
        digs.append(i + 1)
    sol = []
    for i in range(0, n):
        if math.factorial(n - (i + 1)) > k:
            sol.append(digs.pop(0))
            continue
        f = k // math.factorial(n - (i + 1))
        k = k % math.factorial(n - (i + 1))
        sol.append(digs.pop(f))
    # printing answer
    for i in range(0, n):
        if i == n - 1:
            print(sol[i])
        else:
            print(sol[i], end=" ")

for i in sys.stdin:
    line = i.split()
    solution(int(line[0]), int(line[1]))