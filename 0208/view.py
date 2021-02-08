T = 10


for tc in range(1, T+1):
    n = int(input())
    building = list(map(int, input().split()))

    cnt = 0

    for i in range(2, n - 2):
        if building[i] > building[i - 2] and building[i] > building[i - 1]:
            if building[i] > building[i + 1] and building[i] > building[i + 2]:
                cnt += building[i] - max(building[i - 1], building[i - 2], building[i + 1], building[i + 2])

    print(f'#{cnt}')