# 1. 후위 표기식으로 바꾸고
# 2. 후위 표기식 연산

# 1
def post(formula):
    result = ''
    stack = []
    #우선순위
    priority = {'(': 0, '+': 1, '*': 2}

    for f in formula:
        # 연산자면
        if f == '+' or f == '*' or f == '(' or f == ')':
            # 스택이 비어있으면 push
            if len(stack) == 0:
                stack.append(f)

            else:
                if


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

