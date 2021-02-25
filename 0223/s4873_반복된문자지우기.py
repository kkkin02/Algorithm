def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()


t = int(input())

for tc in range(1, t+1):
    string = input()

    #일단 첫번째 글자를 stack에 담아놓고
    stack = [string[0]]
    #그 다음 글자부터 검사
    for i in range(1, len(string)):
        #stack에 요소가 들어있을때, stack의 마지막 글자와 같다면 제거
        if stack and string[i] == stack[-1]:
            pop()
        else:
            push(string[i])

    print(f'#{tc} {len(stack)}')

