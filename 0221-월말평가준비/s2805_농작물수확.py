t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))

    x = n // 2
    cnt = 0
    for i in range(n):
        if i <= x:
            for j in range(i+1):
                cnt += arr[i][x+j]
                cnt += arr[i][x-j]
            cnt -= arr[i][x]
        else:
            for k in range(n-i-1, -1, -1):
                cnt += arr[i][x+k]
                cnt += arr[i][x-k]
            cnt -= arr[i][x]

    print(f'#{tc} {cnt}')
