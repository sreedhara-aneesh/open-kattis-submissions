def solution():
    line1 = input().split()[0]
    line2 = input().split()[0]
    sol = 1
    for i in range(0, len(line1)):
        if line1[i] != line2[i]:
            sol *= 2
    print(sol)

solution()
        
