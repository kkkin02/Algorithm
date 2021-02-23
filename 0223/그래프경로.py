t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    route = []
    for _ in range(e):
        route.append(list(map(int, input().split())))
    s, g = map(int, input().split())

    visited = [0] * (v+1)
    stack = [s]
    visited[s] = 1

    while destination != g:
        for i in route:
            if i[0] == s:
                visited[s] = 1
                destination = i[1]
                if destination == g:
                    result = 1
                    break
                else:
                    if visited[i[1]] == 0:
                        stack.append(s)
                        s = stack[-1]

                    else:
                        stack.pop()
                        s = stack[-1]
        else:
            result = 0

    print(f'#{tc} {result}')
