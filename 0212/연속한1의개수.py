t = int(input())

for tc in range(1, t+1):

    n = int(input())
    numbers = input()

    for i in range(1, n+1):
        if '1'*i in numbers:
            max_cnt = i


    print('#{} {}'.format(tc, max_cnt))