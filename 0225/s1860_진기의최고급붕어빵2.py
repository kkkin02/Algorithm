def isPossible(n, m, k, time):
    # 현재 붕어빵
    fish = 0

    # 손님이 오는 시간
    customer = [0] * 11112
    for t in time:
        customer[t] += 1

    # i가 현재 시간
    for i in range(11112):
        # i가 m의 배수가 될 때마다 k개 생산
        if i>0 and i%m == 0:
            fish += k
        # i 시간에 손님이 오면 손님수만큼 뺀다
        if customer[i] > 0:
            fish -= customer[i]
        # 빼고 나서 음수면 안됨
        if fish < 0:
            return 'Impossible'

    return 'Possible'


t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))

    print(f'#{tc} {isPossible(n, m, k, time)}')


