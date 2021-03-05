t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 행렬을 담을 리스트
    result = []
    # 행렬의 개수
    cnt_matrix = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt_matrix += 1
                # 가로(열)
                cnt_h = 0
                # 세로(행)
                cnt_v = 0
                for k in range(j, n):
                    if arr[i][k] > 0:
                        cnt_h += 1
                    else:
                        break
                for l in range(i, n):
                    if arr[l][j] > 0:
                        cnt_v += 1
                    else:
                        break

                result.append([cnt_v, cnt_h, cnt_v * cnt_h])

                # 이미 센 행렬에 해당하는 값을 0 으로 초기화
                for x in range(i, i+cnt_v):
                    for y in range(j, j+cnt_h):
                        arr[x][y] = 0

    # 카운팅 정렬
    cnt_sort = [0] * 10001
    sort_result = [0] * len(result)

    # 카운팅
    for a in range(len(result)):
        cnt_sort[result[i][]]

