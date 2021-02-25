t= int(input())

for tc in range(1, t+1):
    n = int(input())
    daily = list(map(int, input().split()))

    cnt = 0
    revenue = 0
    total_cost = 0

    for i in range(n):
        if i == n-1:
            revenue += daily[i] * cnt - total_cost
            break

        if daily[i] <= daily[i+1]:
            cnt += 1
            total_cost += daily[i]

        else: # daily[i] > daily[i+1]
            max_daily = daily[i]
            for j in range(i+2, n):
                if daily[j] > max_daily:
                    max_daily = daily[j]

            if daily[i] >= max_daily:
                revenue += daily[i] * cnt - total_cost
                cnt = 0
                total_cost = 0

            else:
                cnt += 1
                total_cost += daily[i]

    print(f'#{tc} {revenue}')
