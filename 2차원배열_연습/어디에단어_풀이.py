t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = 0
    for i in range(n):
        cnt = 0
        #가로검사
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            #연속된 1값이 끝나고 0이 나오거나/ j가 끝값일 때
            if arr[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

        #세로검사
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            #연속된 1값이 끝나고 0이 나오거나/ j가 끝값일 때
            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0
