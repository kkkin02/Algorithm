t = 10

for tc in range(1, t+1):
    input()
    find = input()
    string = input()

    n = len(find)
    m = len(string)
    cnt = 0
    for i in range(m-n+1):
        if find == string[i:i+n]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
