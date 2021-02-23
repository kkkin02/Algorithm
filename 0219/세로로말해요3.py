t = int(input())

for tc in range(1, t + 1):
    arr = []
    for _ in range(5):
        arr.append(input())

    print(f'#{tc}', end=' ')

     # 세로 탐색
    for i in range(15):
        for j in range(5):
            if len(arr[j]) > i:
                print(arr[j][i], end='')
    print()
