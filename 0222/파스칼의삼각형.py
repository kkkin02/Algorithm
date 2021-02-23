t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for l in range(1, n+1):
        arr.append([1] * l)

    print(f'#{tc}')

    for i in range(2, n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    for k in range(n):
        print(*arr[k])