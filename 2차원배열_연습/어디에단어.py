t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            # 가로에서 연속된 1의 개수 카운트
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

        cnt = 0
        for j in range(n):
            # 세로에서 연속된 1의 개수 카운트
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    print(f'#{tc} {result}')