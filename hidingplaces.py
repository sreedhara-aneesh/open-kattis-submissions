def solution():
    board = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            row.append(-1)
        board.append(row)

    raw_pos = input().split()[0]
    pos = [ord(raw_pos[0]) - 97, int(raw_pos[1]) - 1]
    board[pos[0]][pos[1]] = 0

    q = [pos]

    while len(q) != 0:
        pos = q.pop(0)
        cons = [
            [pos[0] + 2, pos[1] + 1],
            [pos[0] + 2, pos[1] - 1],
            [pos[0] - 2, pos[1] + 1],
            [pos[0] - 2, pos[1] - 1],
            [pos[0] + 1, pos[1] + 2],
            [pos[0] + 1, pos[1] - 2],
            [pos[0] - 1, pos[1] + 2],
            [pos[0] - 1, pos[1] - 2]
        ]
        for c in cons:
            if c[0] > 7 or c[0] < 0 or c[1] > 7 or c[1] < 0:
                continue
            if board[c[0]][c[1]] == -1:
                board[c[0]][c[1]] = board[pos[0]][pos[1]] + 1
                q.append(c)        

    max = 0
    max_pos = []

    for i in range(7, -1, -1):
        for j in range(0, 8):
            if board[j][i] > max:
                max_pos = []
                max = board[j][i]
            if board[j][i] == max:
                max_pos.append([j, i])

    print(max, end=' ')
    for pos in max_pos:
        print(f'{chr(pos[0] + 97)}{pos[1] + 1}', end=' ')
    print()

n = int(input().split()[0])
for i in range(0, n):
    solution()