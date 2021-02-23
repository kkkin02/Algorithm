t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    sum_top = sum_bottom = sum_right = sum_left = 0

    for i in range(n):
        for j in range(n):
            #좌상단에서 우하단으로 가는 대각선을 기준으로 위쪽
            if i < j:
                #우상단에서 좌하단으로 가는 대각선 기준 위쪽이 top
                if j < n-i-1:
                    sum_top += arr[i][j]
                    #top을 대칭한 것이 left
                    sum_left += arr[j][i]
                #우상단에서 좌하단으로 가는 대각선 기준 아래쪽이 right
                elif j > n-i-1:
                    sum_right += arr[i][j]
                    #right를 대칭한 것이 bottom
                    sum_bottom += arr[j][i]
                #대각선
                else:
                    continue

            else:
                continue


    max_sum = sum_top
    min_sum = sum_top
    for k in [sum_top, sum_right, sum_left, sum_bottom]:
        if k > max_sum:
            max_sum = k
        if k < min_sum:
            min_sum = k

    result = max_sum - min_sum
    print(f'#{tc} {result}')
