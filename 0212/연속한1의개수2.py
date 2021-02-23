t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input()))

    max_cnt = 0
    cnt = 0
    for i in range(n):
        if a[i] == 1:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0

    if cnt > max_cnt:
        max_cnt = cnt

    print(f'#{tc} {max_cnt}')

