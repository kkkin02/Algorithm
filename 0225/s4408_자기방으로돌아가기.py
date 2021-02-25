t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    corridor = [0] * 201
    for i in arr:
        start = (i[0] + 1) // 2
        end = (i[1] + 1) // 2

        if start > end:
            for j in range(end, start+1):
                corridor[j] += 1

        else:
            for k in range(start, end+1):
                corridor[k] += 1

    max_move = 0
    for c in corridor[1:]:
        if c > max_move:
            max_move = c

    print(f'#{tc} {max_move}')
