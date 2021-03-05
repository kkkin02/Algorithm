def sequence(number):
    for i in range(m):
        p = number.pop(0)
        number.append(p)

    return number

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))

    print(f'#{tc} {sequence(number)[0]}')