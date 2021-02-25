def sudoku(arr):

    # 가로 검증
    for i in range(9):
        check_1 = {}
        for j in range(9):
            if arr[i][j] in check_1.keys():
                return 0
            else:
                check_1[arr[i][j]] = 1

    # 세로 검증
    for i in range(9):
        check_2 = {}
        for j in range(9):
            if arr[j][i] in check_2.keys():
                return 0
            else:
                check_2[arr[j][i]] = 1

    # 사각형 검증
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            check_3 = {}
            for a in range(3):
                for b in range(3):
                    if arr[k+a][l+b] in check_3.keys():
                        return 0
                    else:
                        check_3[arr[k+a][l+b]] = 1

    return 1

t = int(input())

for tc in range(1, t+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    print(f'#{tc} {sudoku(arr)}')
