t = int(input())

for tc in range(1, t+1):
    data = input()

    cards = []
    for _ in range(4):
        # S, D, H, C 순서 0~14까지 카드번호, 0번은 사용안함
        cards.append([0] * 14)

    result = True
    #data를 3칸씩 읽으면 됨
    for i in range(0, len(data), 3):
        num = int(data[i+1] + data[i+2])

        if data[i] == 'S':
            if cards[0][num] == 1:
                result = False
                break
            cards[0][num] = 1
            # 각 무늬별 0번 칸을 카드 개수를 세는 역할로 사용
            cards[0][0] += 1

        elif data[i] == 'D':
            if cards[1][num] == 1:
                result = False
                break
            cards[1][num] = 1
            cards[1][0] += 1

        elif data[i] == 'H':
            if cards[2][num] == 1:
                result = False
                break
            cards[2][num] = 1
            cards[2][0] += 1

        else:
            if cards[3][num] == 1:
                result = False
                break
            cards[3][num] = 1
            cards[3][0] += 1

    if result == False:
        print(f'#{tc} ERROR')

    else:
        print(f'#{tc} {13-cards[0][0]} {13-cards[1][0]} {13-cards[2][0]} {13-cards[3][0]}')

