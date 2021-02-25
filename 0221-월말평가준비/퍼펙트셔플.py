t = int(input())

for tc in range(1, t+1):
    n = int(input())
    deck = input().split()

    print(f'#{tc}', end=' ')

    # 홀수면
    if n%2:
        # 가운데를 기준으로 처음거 하나, 가운데 이후거 하나 이렇게 출력하고
        for i in range(n//2):
            print(deck[i], deck[n//2+1+i], end=' ')
        # 마지막에 가운데거 출력
        print(deck[n//2], end=' ')

    # 짝수면
    else:
        # 처음거 하나, 가운데 이후거 하나 이렇게 짝맞춰서 출력
        for i in range(n//2):
            print(deck[i], deck[n//2+i], end=' ')

    print()