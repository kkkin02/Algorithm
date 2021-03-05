def miro(start, arr):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = []
    for _ in range(16):
        visited.append([0] * 16)

    q = []
    q.append(start)
    r = start[0]
    c = start[1]
    visited[r][c] = 1

    while q:
        p = q.pop(0)
        r = p[0]
        c = p[1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                if arr[nr][nc] == 3:
                    return 1
                else:
                    q.append([nr, nc])
                    visited[nr][nc] = 1

    return 0


for t in range(10):
    tc = int(input())
    arr = []
    for _ in range(16):
        arr.append(list(map(int, input())))

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = [i, j]
                break

    print(f'#{tc} {miro(start, arr)}')

