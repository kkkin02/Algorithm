t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    card = list(map(int, input()))

    result = {}
    for i in range(0, n):
        if card[i] in result.keys():
            result[card[i]] += 1
        else:
            result[card[i]] = 1

    max_k=0
    max_v=0
    for k, v in result.items():
        if v > max_v:
            max_k = k
            max_v = v
        elif v == max_v:
            if k > max_k:
                max_k = k



    print(f'#{tc} {max_k} {max_v}')