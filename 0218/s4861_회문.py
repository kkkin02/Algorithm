t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input())

    print(f'#{tc}', end=' ')

    for i in range(n):
        for j in range(n):
            # 가로확인
            if j + m - 1 < n and arr[i][j] == arr[i][j + m - 1]:
                string = arr[i][j:j + m]
                if string == string[::-1]:
                    print(string)

            # 세로확인
            if j + m - 1 < n and arr[j][i] == arr[j + m - 1][i]:
                string = ''
                for k in range(j, j + m):
                    string += arr[k][i]
                if string == string[::-1]:
                    print(string)
