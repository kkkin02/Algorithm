t = int(input())

for tc in range(1, t+1):
    n, m1, m2 = map(int, input().split())
    block = list(map(int, input().split()))

    if m1 >= m2:
        s = m2
        l = m1
    else:
        s = m1
        l = m2

    blocks = sorted(block)
    blocks = blocks[::-1]

    top_s = []
    top_l = []

    for i in range(0, n-1, 2):
        if len(top_s) == s:
            break
        top_s.append(blocks[i])
        blocks[i] = 0
        top_l.append(blocks[i+1])
        blocks[i+1] = 0

    for j in blocks:
        if j > 0:
            top_l.append(j)

    total_s = 0
    for a in range(1, s+1):
        total_s += top_s[a-1] * a

    total_l = 0
    for b in range(1, l+1):
        total_l += top_l[b-1] * b

    print(f'#{tc} {total_l + total_s}')






