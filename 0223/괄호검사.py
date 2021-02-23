def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()

t = int(input())

for tc in range(1, t+1):
    test = input()

    stack = []

    for i in range(len(test)):
        if test[i] == '(':
            push(test[i])

        elif test[i] == '{':
            push(test[i])

        elif test[i] == ')':
            if pop() == '(':
                result = 1
            else:
                result = 0
                break

        elif test[i] =='}':
            if pop() == '{':
                result = 1
            else:
                result = 0
                break

        if i == len(test)-1:
            if len(stack) == 0:
                result = 1
            else:
                result = 0

    print(f'#{tc} {result}')

