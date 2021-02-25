# 1. 후위 표기식으로 바꾸고
# 2. 후위 표기식 연산

# 1
def post(formula):
    result = ''
    stack = []
    #우선순위
    priority = {'+': 1, '*': 2}

    for f in formula:
        # 연산자면
        if f == '+' or f == '*':
            # 스택이 비어있으면 oush
            if len(stack) == 0:
                stack.append(f)
            # 스택이 비어있지 않으면 스택의 top과 우선순위 비교
            else:
                # 밖에 있는 연산자의 우선순위가 더 작거나 같으면
                if priority[f] <= priority[stack[-1]]:
                    # 스택이 비어있지 않고 우선순위가 작거나 같은동안 pop
                    while len(stack) > 0 and priority[f] <= priority[stack[-1]]:
                        result += stack.pop()
                    # 해당 경우를 다 pop 하고 나면 push
                    stack.append(f)
                # 밖에 있는 연산자의 우선순위가 더 크면 push
                else:
                    stack.append(f)

        # 피연산자면 그냥 출력
        else:
            result += f

    # 스택에 남은게 있으면
    while stack:
        result += stack.pop()

    return result

# 2
def calculator(post):
    stack = []
    operator = ['+', '*']
    for p in post:
        # 연산자면
        if p in operator:
            # stack에 들어있는 마지막 숫자 2개를 계산
            x = int(stack.pop())
            y = int(stack.pop())
            if p == '+':
                stack.append(x + y)
            elif p == '*':
                stack.append(x * y)

        # 피연산자면 stack에 push
        else:
            stack.append(p)

    # stack에 마지막에 남은 값이 결과값
    result = stack.pop()
    return result



t = 10

for tc in range(1, t+1):
    n = int(input())
    formula = input()

    print(f'#{tc}', calculator(post(formula)))

