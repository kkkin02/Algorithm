t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    daily = list(map(int, input().split()))

    max_daily = daily[-1]
    revenue = 0

    for i in range(n - 1, -1, -1):
        if daily[i] > max_daily:
            max_daily = daily[i]

        else:
            revenue += max_daily - daily[i]

    print(f'#{tc} {revenue}')
