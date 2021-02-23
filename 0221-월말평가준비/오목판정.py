t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input()))

    result = 0

    for i in range(n):
        cnt = 0
        #가로
        for j in range(n):
            if arr[i][j] == 'o':
                cnt += 1
            if arr[i][j] =='.' or j == n-1:
                if cnt >= 5:
                    result += 1
                cnt = 0

    for i in range(n):
        #세로
        for j in range(n):
            if arr[j][i] == 'o':
                cnt += 1
            if arr[j][i] =='.' or j == n-1:
                if cnt >= 5:
                    result += 1
                cnt = 0

    #우상단 출발 대각선
    for i in range(n):
        if arr[i][n-i-1] == 'o':
            cnt += 1
        if arr[i][n-i-1] =='.' or i == n-1:
            if cnt >= 5:
                result += 1
            cnt = 0

    #좌상단 출발 대각선
    for i in range(n):
        if arr[i][i] == 'o':
            cnt += 1
        if arr[i][i] == '.' or i == n-1:
            if cnt >= 5:
                result += 1
            cnt = 0

    print(f'#{tc}', end=' ')
    if result >= 1:
        print('YES')0
    else:
        print('NO')