t = int(input())

for tc in range(1, t+1):
    number = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0


    while number % 2 == 0:
        number = number / 2
        a += 1
    while number % 3 == 0:
        number = number / 3
        b += 1
    while number % 5 == 0:
        number = number / 5
        c += 1
    while number % 7 == 0:
        number = number / 7
        d += 1
    while number % 11 == 0:
        number = number / 11
        e += 1

    print(f'#{tc} {a} {b} {c} {d} {e}')


