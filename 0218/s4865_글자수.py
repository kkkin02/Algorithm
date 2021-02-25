t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()

    result = {}
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
               	result[i] = cnt

    max_str = 0
    for v in result.values():
        if v > max_str:
            max_str = v

    print('#{} {}'.format(tc, max_str))


