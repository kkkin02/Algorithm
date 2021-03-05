# 각 행에서 색깔별로 몇개를 바꿔야 하는지를 세고 이를 누적하는 방법

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]

    w = [0] * n
    b = [0] * n
    r = [0] * n

    # 행에서 나와 다른 색깔(바꿔야 하는 색깔)의 개수를 카운트
    for i in range(n):
        for j in range(m):
            if flag[i][j] != 'W':
                w[i] += 1
            if flag[i][j] != 'B':
                b[i] += 1
            if flag[i][j] != 'R':
                r[i] += 1

    # 누적
    for i in range(1, n):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]

    ans = 987654321

    # i는 w의 높이 기준
    # i가 최대일 때 r, b도 한줄씩은 확보되도록
    for i in range(n-2):
        for j in range(i+1, n-1):
            w_cnt = w[i]
            b_cnt = b[j] - b[i] # i줄까지는 w, j줄까지는 b
            r_cnt = r[n-1] - r[j] # 맨 밑에서 j+1줄까지 r

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt

    print(f'#{tc} {ans}')

