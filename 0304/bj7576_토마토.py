def tomato(t, box):
    l = len(t)

    if l == 0:
        return -1
    elif l == n * m:
        return 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[0] * m for _ in range(n)]
    q = []
    for i in t:
        q.append(i)
        visited[i[0]][i[1]] = 1

    while q:
        p = q.pop(0)
        r = p[0]
        c = p[1]

        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0 and visited[nr][nc] == 0:
                box[nr][nc] = 1
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

    result = 0
    for x in range(n):
        for y in range(n):
            if box[x][y] == 0:
                return -1
            elif box[x][y] == 1:
                if visited[x][y] > result:
                    result = visited[x][y]

    return result - 1


m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

t = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            t.append([i, j])
            break


print(tomato(t, box))