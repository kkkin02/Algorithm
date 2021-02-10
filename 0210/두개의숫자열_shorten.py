t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())

    if n >= m:
        fix = list(map(int, input().split()))
        move = list(map(int, input().split()))
    else:
        n, m = m, n
        move = list(map(int, input().split()))
        fix = list(map(int, input().split()))


    result = []
    for i in range(n-m+1):
        total = 0
        for j in range(m):
            total += move[j] * fix[i+j]
        result.append(total)

    max_m = result[0]
    for r in result:
        if r > max_m:
            max_m = r

    print(f'#{tc} {max_m}')




