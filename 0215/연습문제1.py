t = int(input())

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, t+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))

    sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    sum += abs(arr[nr][nc] - arr[i][j])

    print(f'#{tc} {sum}')

