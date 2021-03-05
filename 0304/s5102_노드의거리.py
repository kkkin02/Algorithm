def distance(s, g, v, arr):

    visited = [0] * (v+1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        p = q.pop(0)

        if p == g:
            return visited[p] - 1

        else:
            for i in range(1, v+1):
                if arr[p][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[p] + 1

    return 0


t = int(input())

for tc in range(1, t+1):
    v, e = map(int,input().split())
    edge = []
    for _ in range(e):
        edge.append(list(map(int, input().split())))
    s, g = map(int, input().split())

    # 무향 그래프 만들기
    arr = []
    for _ in range(v+1):
        arr.append([0] * (v+1))

    for e in edge:
        arr[e[0]][e[1]] = 1
        arr[e[1]][e[0]] = 1

    print(f'#{tc} {distance(s, g, v, arr)}')

