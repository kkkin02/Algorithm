#우선순위
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

formula = input()
stack = []

for f in formula:
    if f == '+' or f == '*' or f == '-' or f == '/':
        if len(stack) == 0:
            stack.append(f)
        else:
            if icp[f] > isp[stack[-1]]:
                stack.append(f)
            else:
                while icp[f] < isp[stack[-1]]:
                    p = stack.pop()
                    print(p, end=' ')
                stack.append(f)


    else:
        print(f, end=' ')