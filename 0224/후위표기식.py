formula = '2+3*4/5'

stack = []

for f in formula:
    if f == '+' or f == '*' or f == '-' or f == '/':
        stack.append(f)
    else:
        print(f, end=' ')

while stack:
    s = stack.pop()
    print(s, end=' ')