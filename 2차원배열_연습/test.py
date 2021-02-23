t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    max_rec = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                width = 1
                height = 1
                for k in range(i+1, n):
                    #행에서 1이 끝날때까지
                    while arr[i][k] == 1:
                        width += 1
    print(width)