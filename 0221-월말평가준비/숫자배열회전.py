def rotation(arr):
    rotate = []
    for i in range(n):
        row = []
        for j in range(n-1, -1, -1):
            row.append(arr[j][i])
        rotate.append(row)

    return rotate


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().split())


    arr90 = rotation(arr)
    arr180 = rotation(arr90)
    arr270 = rotation(arr180)

    result = []

    print(f'#{tc}')

    for i in range(n):
        for j in range(n):
            print(arr90[i][j], end='')
        print('', end=' ')
        for j in range(n):
            print(arr180[i][j], end='')
        print('', end=' ')
        for j in range(n):
            print(arr270[i][j], end='')
        print('', end=' ')
        print()




