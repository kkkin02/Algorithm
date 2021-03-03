def isPossible(n, m, k, time):
    # 초당 잔여 붕어빵
    fish = [0] * 111111

    for i in range(m, max(time), m):
        for j in range(i, i+m+1):
            fish[j] += fish[i] + k

    for t in time:
        for l in range(t, max(time)):
            fish[l] -= 1
            if fish[l] < 0:
                return 'Impossible'
            else:
                continue

    return 'Possible'

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))

    print(f'#{tc} {isPossible(n, m, k, time)}')


