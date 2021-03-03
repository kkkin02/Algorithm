def miro(maze, start):
    # 상하좌우 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    d = 0

    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = 1

    while stack:
        p = stack.pop()
        r = p[0]
        c = p[1]
        last = maze[r][c]

        if last == 3:
            return 1

        for i in range(4):
            if 0 <= r + dr[i] < n and 0 <= c + dc[i] < n and maze[r + dr[i]][c + dc[i]] != 1 and visited[r + dr[i]][c + dc[i]] == 0:
                stack.append([r + dr[i], c + dc[i]])
                visited[r][c] = 1


    return 0


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    maze = []
    visited = []
    for _ in range(n):
        maze.append(list(map(int, input())))
        visited.append([0] * n)

    # 미로 끝 찾기
    for a in range(n):
        for b in range(n):
            if maze[a][b] == 2:
                start = [a, b]
                break

    print(f'#{tc} {miro(maze, start)}')


