for t in range(10):
    tc = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    #상 좌 우
    dr = [-1, 0, 0]
    dc = [0, -1, 1]

    #현재방향
    dir = 0

    # 도착지점 찾기
    for i in range(100):
        if arr[99][i] == 2:
            r = 99
            c = i
            break

    # 도착지점에서 시작해서 행이 0이 될 때까지
    while r > 0:

        #좌측에 길이 있을 때
        if 0<c and arr[r][c-1] == 1:
            dir = 1
            while 0<c and arr[r][c-1] == 1:
                r += dr[dir]
                c += dc[dir]
            #좌측으로 계속 가다가 길이 막혔을 때는 다시 위로 이동
            dir = 0


        #우측에 길이 있을 때
        elif c<99 and arr[r][c+1] == 1:
            dir = 2
            while c<99 and arr[r][c+1] == 1:
                r += dr[dir]
                c += dc[dir]
            #우측으로 계속 가다가 길이 막혔을 때는 다시 위로 이동
            dir = 0

        # 위로 이동
        r += dr[dir]
        c += dc[dir]

    print(f'#{tc} {c}')
