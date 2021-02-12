t = int(input())

for tc in range(1, t+1):
    n = int(input())
    carrots = list(map(int, input().split()))

    cnt = 1
    max_cnt = 1

    for i in range(n-1):
        if carrots[i] < carrots[i+1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt

        else:
            cnt = 1

    print('#{} {}'.format(tc, max_cnt))