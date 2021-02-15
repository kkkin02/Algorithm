for t in range(10):
    tc = input()
    arr = []
    for number in range(100):
        arr.append(list(map(int, input().split())))

    result = []
    #열의 합
    for a in range(100):
        total_col = 0
        for b in range(100):
            total_col += arr[b][a]
        result.append(total_col)

    #행의 합
    for c in range(100):
        total_row = 0
        for d in range(100):
            total_row += arr[c][d]
        result.append(total_row)

    #대각선의 합
    total_cross = 0
    for e in range(100):
        total_cross += arr[e][e]
    result.append(total_cross)

    #반대 대각선의 합
    total_cross_re = 0
    for f in range(100):
        total_cross_re += arr[f][99-f]
    result.append(total_cross_re)

    max_sum = result[0]
    for r in result:
        if r > max_sum:
            max_sum = r

    print(f'#{tc} {max_sum}')

