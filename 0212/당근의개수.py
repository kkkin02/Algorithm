t = int(input())

for tc in range(1, t+1):
    n = int(input())
    carrots = list(map(int, input().split()))

    max_c = carrots[0]
    max_idx = 0

    for i in range(n):
        if carrots[i] > max_c:
            max_c = carrots[i]
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx+1, max_c))