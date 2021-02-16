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
                width = 0
                height = 0
                #해당 행에서 1의 개수
                for k in range(j, n):
                    if arr[i][k] == 1:
                        width += 1
                    #연속된 1이 끝날 때까지가 가로
                    else:
                        break
                #해당 열에서 1의 개수
                for l in range(i, n):
                    if arr[l][j] == 1:
                        height += 1
                    #연속된 1이 끝날 때까지가 세로
                    else:
                        break
                #크기 비교
                if width * height > max_rec:
                    max_rec = width * height

    print(f'#{tc} {max_rec}')

