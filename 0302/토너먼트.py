def rsp(a, b):
    if a[1] == 1:
        if b[1] == 1:
            if a[0] < b[0]:
                return a
            else:
                return b
        elif b[1] == 2:
            return b
        else:
            return a

    elif a[1] == 2:
        if b[1] == 1:
            return a
        elif b[1] == 2:
            if a[0] < b[0]:
                return a
            else:
                return b
        else:
            return b
    else:
        if b[1] == 1:
            return b
        elif b[1] == 2:
            return a
        else:
            if a[0] < b[0]:
                return a
            else:
                return b


def tournament(n, i, j, card):
    if n == 2:
        return rsp(card[0], card[1])

    elif n == 3:
        return rsp(tournament(2, i, j-1, card[:2]), card[2])

    else:
        if n % 2:
            d = (i + j) // 2
            return rsp(tournament(n // 2 + 1, i, d, card[:d]), tournament(n // 2, d + 1, j, card[d:]))

        else:
            d = (i+j) // 2
            return rsp(tournament(n/2 , i, d, card[:d]), tournament(n/2, d+1, j, card[d:]))


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    card = list(map(int, input().split()))
    cards = []
    for c in enumerate(card, 1):
        cards.append(c)

    i = 1
    j = n

    print(f'#{tc} {tournament(n, i, j, cards)[0]}')
