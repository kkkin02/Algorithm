t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    max_cnt = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m):
                for l in range(m):
                    cnt += arr[i+k][j+l]

            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt')

