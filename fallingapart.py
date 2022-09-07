def solution():
    line = input().split()
    fragments = int(line[0])
    line = input().split()
    nums = []
    for i in range(0, fragments):
        nums.append(int(line[i]))
    nums.sort(reverse=True)
    alice = 0
    bob = 0
    aliceTurn = True
    for i in range(0, fragments):
        if aliceTurn:
            alice += nums[i]
        else:
            bob += nums[i]
        aliceTurn = not aliceTurn
    print(f"{alice} {bob}")

solution()