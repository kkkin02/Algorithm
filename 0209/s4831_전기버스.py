t = int(input())

for tc in range(1, t + 1):

    k, n, m = map(int, input().split())
    b = list(map(int, input().split()))
    bus_stop = [0] + b + [n]

    last = 0
    cnt = 0
    for i in range(1, m+2):
        if bus_stop[i] - bus_stop[i-1] > k:
            cnt = 0
            break

        if bus_stop[i] - bus_stop[last] > k:
            last = i-1
            cnt += 1


    print(f'#{tc} {cnt}')


