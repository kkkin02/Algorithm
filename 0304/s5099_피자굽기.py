def bake(pizza):

    # 화덕 채우기
    oven = pizza[:n]

    # 다음에 들어갈 피자의 인덱스
    idx = n

    # 화덕에 피자가 한개만 남을 때까지
    while len(oven) > 1:
        # 화덕 맨 처음에 있는 피자 확인
        p = oven.pop(0)
        p[1] = p[1] // 2

        # 치즈가 다 녹았으면
        if p[1] == 0:
            # 구울 피자가 더 남아있으면 집어넣음
            if idx < m:
                oven.append(pizza[idx])
                idx += 1
            else:
                continue

        # 안녹았으면 다시 집어넣음
        else:
            oven.append(p)

    return oven.pop()


t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    cheese = list(map(int, input().split()))
    pizza = []
    for p, c in enumerate(cheese, 1):
        # p: 피자 번호 c: 치즈
        pizza.append([p, c])

    print(f'#{tc} {bake(pizza)[0]}')
