t = int(input())

for tc in range(1, t+1):
    input()
    numbers = input().split()

    num_str = {
        'ZRO': 0,
        'ONE': 0,
        'TWO': 0,
        'THR': 0,
        'FOR': 0,
        'FIV': 0,
        'SIX': 0,
        'SVN': 0,
        'EGT': 0,
        'NIN': 0
    }

    for i in numbers:
        if i in num_str.keys():
            num_str[i] += 1

    print('#{}'.format(tc))
    for k, v in num_str.items():
        for j in range(v):
            print(k, end=' ')
    print()



