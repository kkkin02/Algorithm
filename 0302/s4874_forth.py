def forth(formula):
    stack = []
    operator = ['+', '-', '*', '/']

    for f in formula:
        if f == '.':
            if len(stack) == 1:
                return int(stack.pop())
            else:
                break

        # 연산자일 때
        elif f in operator:
            if len(stack) < 2:
                break

            # 숫자 두 개 꺼내서 연산하고 push
            x = int(stack.pop())
            y = int(stack.pop())

            if f == '+':
                stack.append(y + x)
            elif f == '*':
                stack.append(y * x)
            elif f == '-':
                stack.append(y - x)
            else:
                stack.append(y / x)

        # 숫자일 때
        else:
            stack.append(f)

    return 'error'


t = int(input())

for tc in range(1, t + 1):
    formula = input().split()

    print(f'#{tc} {forth(formula)}')