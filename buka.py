operand1 = input().split()[0]
operation = input().split()[0]
operand2 = input().split()[0]

pow1 = len(operand1) - 1
pow2 = len(operand2) - 1

if operation == '*':
    print('1' + ('0' * (pow1 + pow2)))
else:
    if pow1 == pow2:
        print('2' + ('0' * (pow1)))
    else:
        maxpow = max(pow1, pow2)
        minpow = min(pow1, pow2)
        print('1' + ('0' * (maxpow - minpow - 1)) + '1' + ('0' * (minpow)))
