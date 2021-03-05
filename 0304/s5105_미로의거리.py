def shortest(n, arr, r, c):
    # 상하좌우 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = []
    for _ in range(n):
        visited.append([0] * n)

    q = []
    q.append([r, c])
    visited[r][c] = 1

    while q:
        p = q.pop(0)
        r = p[0]
        c = p[1]

        # 상하좌우를 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 목적지인 3을 만나면 직전의 visited 값을 return
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 3:
                # 시작점의 visited 값이 1이기 때문에 실제 거리는 1을 빼준다
                return visited[r][c] - 1

            # 통로가 있으면 큐에 append하고 visited를 거리값으로 저장
            elif 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

    # 큐를 다 탐색할 때까지 목적지에 도달하지 못하면
    return 0


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                r = i
                c = j
                break

    print(f'#{tc} {shortest(n, arr, r, c)}')

