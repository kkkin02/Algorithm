def Parentheses(arr):
    stack = []
    P = {'(': ')', '{': '}', '[': ']'}
    for i in arr:
        if i in P:
            stack.append(i)
        elif i in P.values():
            if stack:
                s = stack.pop()
                if P[s] != i:
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return 1


T = int(input())
for test in range(1, T + 1):
    arr = input()
    print(f'#{test}', Parentheses(arr))