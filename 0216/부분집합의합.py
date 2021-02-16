t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(range(1, 13))

    result = 0
    for i in range(0,2**12):
        subset = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j) != 0:
                subset += arr[j]
                cnt += 1
        if cnt == n and subset == k:
            result += 1

    print(f'#{tc} {result}')


