t = int(input())

for tc in range(1, t+1):
    number = int(input())

    result = ''

    for i in [2, 3, 5, 7, 11]:
        cnt = 0
        while number % i == 0:
            number = number // i
            cnt += 1
        result += str(cnt)

    result = ' '.join(result)
    print(f'#{tc} {result}')


