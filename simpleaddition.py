n1 = list(input().split()[0])
n2 = list(input().split()[0])

out = ''
carry = 0

while len(n1) != 0 or len(n2) != 0:
    d1 = d2 = 0
    if len(n1) != 0:
        d1 = int(n1.pop())
    if len(n2) != 0:
        d2 = int(n2.pop())
    out = str((d1 + d2 + carry) % 10) + out
    carry = (d1 + d2 + carry) // 10

if carry != 0:
    out = str(carry) + out

print(out)