def solution():
    input()
    segments = input().split()
    red = []
    blue = []
    for segment in segments:
        if segment[-1] == 'R':
            red.append(int(segment[0:-1]))
        else:
            blue.append(int(segment[0:-1]))
    red.sort(reverse=True)
    blue.sort(reverse=True)
    length = 0
    for i in range(0, min(len(red), len(blue))):
        length += red[i] - 1
        length += blue[i] - 1
    return length

cases = int(input().split()[0])
for i in range(0, cases):
    print(f"Case #{i + 1}: {solution()}")