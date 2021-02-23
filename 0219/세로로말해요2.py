t = int(input())

for tc in range(1, t + 1):
    arr = []
    for _ in range(5):
        arr.append(input())

    print(f'#{tc}', end=' ')

    # 제일 긴 문자열 찾기
    max_string = 0
    for a in arr:
        if len(a) > max_string:
            max_string = len(a)

    # 세로 탐색
    for i in range(max_string):
        for j in range(5):
            if len(arr[j]) > i:
                print(arr[j][i], end='')
    print()


