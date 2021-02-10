t = int(input())

for tc in range(1, t+1):

    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(n-1):
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print(f'#{tc}', end=' ')
    for number in numbers:
        print(f'{number}', end=' ')

    print()
