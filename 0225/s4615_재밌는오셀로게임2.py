def othello(arr, n, r, c, p):
    # input 에서는 첫칸이 1이라서 인덱스를 맞추기 위해 1을 빼줌
    r = r-1
    c = c-1

    # 상하좌우대각선 탐색할 것임
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]

    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        change = []
        # 행열값이 범위 안에 있고, 빈칸이 아닐 때
        while 0 <= rr < n and 0 <= cc < n and arr[rr][cc] > 0 :
                # 내 돌과 색이 다르면
                if arr[rr][cc] != p:
                    # 색을 바꿔줄 리스트에 담고
                    change.append([rr, cc])
                    # 다음칸 탐색
                    rr += dr[i]
                    cc += dc[i]

                # 내 돌과 색이 같은 돌을 만나면
                elif arr[rr][cc] == p:
                    # 내가 놓을 자리와 내 돌 사이에 상대의 돌이 있을 때만
                    if len(change) != 0:
                        # 그 자리에 돌을 놓을 수 있고
                        arr[r][c] = p
                        # 사이에 있는 돌은 내 돌이 됨
                        for k in change:
                            arr[k[0]][k[1]] = p
                        break

                    # 내가 놓을 자리와 내 돌 사이에 상대의 돌이 없으면 다음 방향 탐색
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