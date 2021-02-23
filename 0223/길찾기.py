def f(n):
    stack = []
    visited = [0] * 99
    stack.append(0)
    visited[0] = 1

    while stack:  # 스택이 비어있지 않으면
        last_n = stack.pop()  # 방문할 목록에서 마지막에 기록된 노드를 꺼내서
        # 방문한 노드가 목적지 g인지 확인
        if last_n == 99:
            return 1
        # 모든 노드에 대해, 현재 노드에서 방문할 수 있는 곳인지 검토

        for i in range(n):
            if route1[last_n] != 0 and visited[last_n] == 0:
                stack.append(route1[last_n])
                visited[route1[last_n]] = 1
            elif route2[last_n] != 0 and visited[last_n] == 0:
                stack.append(route2[last_n])
                visited[route2[last_n]] = 1
    return 0  # 목적지에 도달하지 못하고, 탐색할 노드가 더이상 없는 경우


for _ in range(1):
    tc, n = map(int, input().split())
    node = list(map(int, input().split()))

    route1 = [0] * 100
    route2 = [0] * 100
    for i in range(0, len(node) - 1, 2):
        if route1[node[i]] == 0:
            route1[node[i]] = node[i + 1]
        else:
            route2[node[i]] = node[i + 1]

    print(f'#{tc} {f(n)}')


