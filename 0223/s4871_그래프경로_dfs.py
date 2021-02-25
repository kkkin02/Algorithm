
def f(s, g, v): # s에서 g에 도착할 수 있는지 확인하는 함수
    # 중복없이 빠짐없이 탐색하는 dfs
    # 스택생성
    stack = []
    #방문기록표 생성
    visited = [0] * (v+1)
    stack.append(s)
    visited[s] = 1

    while stack: # 스택이 비어있지 않으면
        n = stack.pop() # 방문할 목록에서 마지막에 기록된 노드를 꺼내서
        # 방문한 노드가 목적지 g인지 확인
        if n == g:
            return 1
        # 모든 노드에 대해, 현재 노드에서 방문할 수 있는 곳인지 검토
        for i in range(1, v+1):
            if route[n][i] == 1 and visited[i] == 0: # 현재 노드가 n, 가려고하는 노드가 i
                stack.append(i)
                visited[i] = 1
    return 0 # 목적지에 도달하지 못하고, 탐색할 노드가 더이상 없는 경우



t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    route = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        e1, e2 = map(int, input().split())
        route[e1][e2] = 1
    s, g = map(int, input().split())

    print(f'#{tc} {f(s, g, v)}')