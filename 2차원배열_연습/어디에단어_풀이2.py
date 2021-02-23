t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        #행의 끝에 0을 붙여줌
        arr.append(list(map(int, input().split()))+[0])
    #열의 끝에 0을 붙여줌
    #그니까 우측이랑 하단에 0으로 삥 둘러줌
    arr.append([0]*(n+1))

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n+1):
            # 가로에서 연속된 1의 개수 카운트
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0

        for j in range(n+1):
            # 세로에서 연속된 1의 개수 카운트
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0


    print(f'#{tc} {result}')