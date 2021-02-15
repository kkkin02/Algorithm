# sum 쓰지 않고
t = int(input())

for tc in range(1, t+1):

    n = int(input())
    sp_numbers = list(map(int, input().split()))

    stem = []
    s_len = 1
    s_num = 0
    for i in range(n-1):
        if sp_numbers[i] < sp_numbers[i+1]:
            s_len += 1
            s_num += sp_numbers[i]
        else:
            if s_len >= 2:
                stem.append([s_len, s_num + sp_numbers[i] ])
                s_len = 1
                s_num = 0
    if s_len >= 2:
        stem.append([s_len, s_num + sp_numbers[n-1]])

    max_len = 0
    max_sum = 0
    for s in stem:
        if s[0] > max_len:
            max_len = s[0]
            max_sum = s[1]
        elif s[0] == max_len:
            if s[1] > max_sum:
                max_sum = s[1]


    print(f'#{tc} {len(stem)} {max_sum}')



