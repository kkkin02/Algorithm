t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    max_n=a[0]
    min_n=a[0]

    for i in range(1, n):
        if a[i] > max_n:
            max_n = a[i]

        elif a[i] < min_n:
            min_n = a[i]

    result = max_n - min_n
    print(f'#{tc} {result}')