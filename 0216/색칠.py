t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(10):
        arr.append([0]*10)

    for i in range(n):
        color = list(map(int, input().split()))
        for a in range(color[0], color[2]+1):
            for b in range(color[1], color[3]+1):
                arr[a][b] += color[4]

    cnt = 0
    for j in range(10):
        for k in range(10):
            if arr [j][k] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))