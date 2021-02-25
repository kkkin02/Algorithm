def othello(arr, n, r, c, p):
    r = r-1
    c = c-1

    # 상하좌우대각선 탐색
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]

    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        change = []
        while 0 <= rr < n and 0 <= cc < n and arr[rr][cc] > 0 :
                if arr[rr][cc] != p:
                    change.append([rr, cc])
                    rr += dr[i]
                    cc += dc[i]

                elif arr[rr][cc] == p:
                    if len(change) != 0:
                        arr[r][c] = p
                        for k in change:
                            arr[k[0]][k[1]] = p
                        break

                    else:
                        break

    return arr


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append([0] * n)

    # 최초 돌 세팅
    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 2
    arr[n//2-1][n//2] = arr[n//2][n//2-1] = 1

    for _ in range(m):
        r, c, p = map(int, input().split())
        arr = othello(arr, n, r, c, p)

    cnt_B = 0
    cnt_W = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                cnt_B += 1
            elif arr[x][y] == 2:
                cnt_W += 1

    print(f'#{tc} {cnt_B} {cnt_W}')