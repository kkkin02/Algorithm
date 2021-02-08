
T = 10


for tc in range(1, T+1):
    n = int(input())
    building = list(map(int, input().split()))

    cnt = 0

    for i in range(2, n - 2):
        if building[i] > building[i - 2] and building[i] > building[i - 1] and building[i] > building[i + 1] and building[i] > building[i + 2]:
            b_list = []
            b_list.append(building[i - 1])
            b_list.append(building[i + 1])
            b_list.append(building[i + 2])
            max_n = building[i-2]
            for j in b_list:
                if max_n < j:
                    max_n = j

            cnt += building[i] - max_n

    print(f'#{tc} {cnt}')