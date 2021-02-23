T = int(input())

for t in range(1, T+1):
    tc, n = map(str, input().split())
    n = int(n)
    a = input().split()

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    result = []
    for i in numbers:
        for j in a:
            if j == i:
                result.append(j)

    print(tc)
    print(*result)





