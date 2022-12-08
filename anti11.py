def case(n):
    nums = [1, 1]
    for i in range(2, n + 2):
        nums.append(nums[i - 1] + nums[i - 2])
    print(nums[-1] % (10 ** 9 + 7))

T = int(input().split()[0])

for i in range(0, T):
    n = int(input().split()[0])
    case(n)