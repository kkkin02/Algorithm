# 1가위  2바위  3보
# 가위바위보에서 이긴 사람 or 비겼을 때 번호 작은사람 return
# 1, 2  ->  2   /   2, 3  ->  3   /  3, 1  ->  1
def rsp(a, b):
    if a[1] == b[1]:
        if a[0] < b[0]:
            return a
        else:
            return b
    elif a[1] > b[1]:
        if a[1] == 3 and b[1] == 1:
            return b
        else:
            return a
    else:
        if b[1] == 3 and a[1] == 1:
            return a
        else:
            return b


def tournament(card):
    # 카드가 한 장일 때는 그 카드 반환
    if len(card) == 1:
        return card[0]

    # 카드가 두 장일 때는 두 카드 가위바위보
    elif len(card) == 2:
        return rsp(card[0], card[1])

    # 카드가 두 장 이상일 때는 반절을 나눠서 반절 내에서 다시 가위바위보
    elif len(card) > 2:
        d = (len(card) + 1) // 2
        l = tournament(card[:d])
        r = tournament(card[d:])
        return rsp(l, r)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    card = list(map(int, input().split()))

    # 인덱스 1부터 인덱스값과 카드값을 같이 저장
    cards = []
    for c in enumerate(card, 1):
        cards.append(c)

    # 최종 승리한 튜플에서 인덱스 값을 출력
    print(f'#{tc} {tournament(cards)[0]}')

