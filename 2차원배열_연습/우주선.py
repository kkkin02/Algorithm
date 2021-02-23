t = int(input())

for tc in range(1, t+1):
    n, m, k, h = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0

    for i in range(1, n-1):
        for j in range(1,m-1):
            max_position = 0
            min_position = 100
            for l in range(8):
                if arr[i+dr[l]][j+dc[l]] > max_position:
                    max_position = arr[i+dr[l]][j+dc[l]]
                if arr[i+dr[l]][j+dc[l]] < min_position:
                    min_position = arr[i+dr[l]][j+dc[l]]
            if max_position - min_position <= k and arr[i][j] >= min_position and arr[i][j] - min_position <= h:
                cnt += 1

    print(f'#{tc} {cnt}')