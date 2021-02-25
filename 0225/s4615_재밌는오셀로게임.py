t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append([0] * n)

    # 최초 돌 세팅
    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 'W'
    arr[n//2-1][n//2] = arr[n//2][n//2-1] = 'B'

    # 상하좌우대각선 탐색
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]

    for i in range(m):
        r, c, p = map(int, input().split())
        # 인덱스와 맞추기 위해서
        r = r-1
        c = c-1

        # 칸이 비어있을 때
        if arr[r][c] == 0:
            # B일때
            if p == 1:
                # 놓을 자리의 상하좌우대각선 탐색
                for j in range(8):
                    for k in range(2, n):
                        if 0 <= r + dr[j] * k < n and 0 <= c + dc[j] * k < n:
                            if arr[r+dr[j]*k][c+dc[j]*k] == 0:
                                break
                            # 놓을 자리에서 상하좌우대각선으로 1칸이상 떨어진 곳에 B돌이 있으면
                            elif arr[r+dr[j]*k][c+dc[j]*k] == 'B':
                                # 놓을 자리와 그 B돌 사이에 W돌이 있는지 확인
                                for l in range(1, k):
                                    if arr[r + dr[j] * l][c + dc[j] * l] == 0:
                                        break
                                    # 있으면 그 자리에 놓을 수 있고, W돌들은 B돌로 바꿈
                                    if arr[r+dr[j]*l][c+dc[j]*l] == 'W':
                                        arr[r][c] = 'B'
                                        arr[r + dr[j] * l][c + dc[j] * l] = 'B'

            # W일때
            else:
                for j in range(8):
                    for k in range(2, n):
                        if 0 <= r + dr[j] * k < n and 0 <= c + dc[j] * k < n:
                            if arr[r+dr[j]*k][c+dc[j]*k] == 0:
                                break
                            elif arr[r+dr[j]*k][c+dc[j]*k] == 'W':
                                for l in range(1, k):
                                    if arr[r + dr[j] * l][c + dc[j] * l] == 0:
                                        break
                                    elif arr[r+dr[j]*l][c+dc[j]*l] == 'B':
                                        arr[r][c] = 'W'
                                        arr[r + dr[j] * l][c + dc[j] * l] = 'W'

        # 칸이 비어있지 않으면 돌을 못놓고 지나감
        else:
            continue

    cnt_B = 0
    cnt_W = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'B':
                cnt_B += 1
            elif arr[x][y] == 'W':
                cnt_W += 1

    print(f'#{tc} {cnt_B} {cnt_W}')
