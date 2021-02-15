t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1<<n):
        sub = []
        for j in range(n):
            if i & (1<<j):
                sub.append(arr[j])

        if sum(sub) == 0 and len(sub) != 0:
            result = 1
            break
        else:
            result = 0

    print(f'#{tc} {result}')

