t = int(input())

for tc in range(1, t+1):
    n = int(input())
    deck = input().split()

    print(f'#{tc}', end=' ')
    if n%2:
        for i in range(n//2):
            print(deck[i], deck[n//2+1+i], end=' ')
        print(deck[n//2])

    else:
        for i in range(n//2):
            print(deck[i], deck[n//2+i], end=' ')


    print()