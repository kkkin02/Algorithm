t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    max_length = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt_a = 0
                for k in range(i, n):
                    if arr[k][j] == 1:
                        cnt_a += 1
                    else:
                        break
                    #cnt_a가 1이면 cnt_a가 폭, cnt_b가 길이
                    if cnt_a == 1:
                        cnt_b = 0
                        for l in range(j, m):
                            if arr[i][l] == 1:
                                cnt_b += 1
                            else:
                                break
                        if cnt_b > max_length:
                            max_length = cnt_b
                    #cnt_a가 1보다 크면 cnt_a가 길이, cnt_b가 폭
                    elif cnt_a > 1:
                        if cnt_a > max_length:
                            max_length = cnt_a

    print(f'#{tc} {max_length}')