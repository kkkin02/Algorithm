def f(s, g, v):
    visited = [0] * (v + 1)
    stack = [s]
    visited[s] = 1

    while stack:
        p = stack.pop()

        if p == g:
            return 1
            break

        for i in range(len(route)):
            if p == route[i][0] and visited[route[i][1]] == 0:
                stack.append(route[i][1])
                visited[route[i][1]] = 1

    return 0

t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    route = []
    for _ in range(e):
        route.append(list(map(int, input().split())))
    s, g = map(int, input().split())

    print(f'#{tc} {f(s, g, v)}')
