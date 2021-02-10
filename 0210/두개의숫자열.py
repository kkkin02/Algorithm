t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n >= m:
        move = b
        fix = a
    elif n < m:
        move = a
        fix = b

    result = []
    for i in range(len(fix) - len(move) + 1):
        total = 0
        for j in range(len(move)):
            total += move[j] * fix[i + j]
        result.append(total)

    max_m = result[0]
    for r in result:
        if r > max_m:
            max_m = r

    print(f'#{tc} {max_m}')