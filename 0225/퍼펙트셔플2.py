t = int(input())

for tc in range(1, t+1):
    n = int(input())
    deck = input().split()

    if n % 2:
        p = n//2 + 1
        deck1 = deck[:p]
        deck2 = deck[p:]
        # deck1의 홀수번 인덱스에 deck2를 끼워넣기
        for i in range(n//2):
            deck1.insert(i*2+1, deck2[i])

    else:
        p = n//2
        deck1 = deck[:p]
        deck2 = deck[p:]
        #deck1의 홀수번 인덱스에 deck2를 끼워넣기
        for i in range(p):
            deck1.insert(i*2+1, deck2[i])

    print(f'#{tc}', *deck1)