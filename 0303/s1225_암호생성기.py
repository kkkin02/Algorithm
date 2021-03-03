def code_maker(code):
    cnt = 0

    while True:
        p = code.pop(0)
        n = p - (cnt % 5 + 1)

        if n <= 0:
            code.append(0)
            break

        else:
            code.append(n)
            cnt += 1

    return code

T = 10

for t in range(1, T+1):
    tc = int(input())
    code = list(map(int, input().split()))

    print(f'#{tc}', *code_maker(code))