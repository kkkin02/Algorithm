t = int(input())

for tc in range(1, t+1):

    n = int(input())
    sp_numbers = list(map(int, input().split()))

    stem = []
    s_len = 0
    for i in range(n-1):
        if sp_numbers[i] < sp_numbers[i+1]:
            s_len += 1
        else:
            if s_len >= 1:
                stem.append(sp_numbers[i-s_len: i+1])
                s_len = 0
    if s_len >= 1:
        stem.append(sp_numbers[n-s_len-1:])


    max_len = 0
    max_sum = 0
    for j in stem:
        if len(j) > max_len:
            max_len = len(j)
            max_sum = sum(j)
        elif len(j) == max_len:
            if sum(j) > max_sum:
                max_sum = sum(j)


    print(f'#{tc} {len(stem)} {max_sum}')



