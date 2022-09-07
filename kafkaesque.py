def solution():
    sigs = int(input().split()[0])
    prev = 0
    runs = 1
    for i in range(0, sigs):
        curr = int(input().split()[0])
        if curr < prev:
            runs += 1
        prev = curr
    print(runs)

solution()