info = input().split()[0]

ls0 = 0 # len longest substring of 0s

cs0 = 0

for c in list(info):
    if c == '0':
        cs0 += 1
    else:
        ls0 = max(ls0, cs0)
        cs0 = 0

print(ls0 // 2 + ls0 % 2)