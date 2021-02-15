t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append([0]*N)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    dir = 0
    i = j = 0
    cnt = 1

    while True:
        arr[i][j] = cnt
        cnt += 1
        i += dr[dir]
        j += dc[dir]

        if i < 0 or i >= N or j < 0 or j >= N:
            i -= dr[dir]
            j -= dc[dir]
            if dir < 3:
                dir += 1
            else:
                dir = 0

            i += dr[dir]
            j += dc[dir]


        if cnt == N**2+1:
            break

    print(f'#{tc}')
    for k in range(N):
        for l in range(N):
            print(arr[k][l], end=' ')
        print()




