t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    section = list(map(int, input().split()))

    max_m = sum(section[0:m])
    min_m = sum(section[0:m])

    for i in range(n-m+1):
        sum_m = 0
        for s in section[i: i+m]:
            sum_m += s

        if sum_m > max_m:
            max_m = sum_m

        elif sum_m < min_m:
            min_m = sum_m

    result = max_m - min_m
    print(f'#{tc} {result}')

